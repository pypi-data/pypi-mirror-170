import json
from datetime import datetime, timedelta

import django
import pytest
from asgiref.sync import sync_to_async

from tests.demo_app.controllers import (
    AutoGenCrudAPIController,
    AutoGenCrudSomeFieldsAPIController,
    EventSchema,
)
from tests.demo_app.models import Category, Client, Event, Type

dummy_data = dict(
    title="AsyncAdminAPIEvent",
    start_date=str(datetime.now().date()),
    end_date=str((datetime.now() + timedelta(days=5)).date()),
)


@pytest.mark.skipif(django.VERSION < (3, 1), reason="requires django 3.1 or higher")
@pytest.mark.django_db
class TestAutoCrudAdminAPI:
    async def test_crud_default_get_all(self, transactional_db, easy_api_client):
        client = easy_api_client(AutoGenCrudAPIController)

        object_data = dummy_data.copy()
        object_data.update(title=f"{object_data['title']}_get_all")

        event = await sync_to_async(Event.objects.create)(**object_data)
        type = await sync_to_async(Type.objects.create)(name="Type")
        category = await sync_to_async(Category.objects.create)(
            title="Category for Unit Testings"
        )
        client_a = await sync_to_async(Client.objects.create)(
            name="Client A for Unit Testings", key="A"
        )
        client_b = await sync_to_async(Client.objects.create)(
            name="Client B for Unit Testings", key="B"
        )
        event.category = category
        event.type = type
        await sync_to_async(event.save)()
        await sync_to_async(event.owner.set)([client_a, client_b])

        response = await client.get(
            "/get_all", query=dict(maximum=100, filters=json.dumps(dict(id__gte=1)))
        )
        assert response.status_code == 200

        data = response.json().get("data")
        assert data[0]["title"] == "AsyncAdminAPIEvent_get_all"
        assert data[0]["type"] == type.id

        event_schema = json.loads(EventSchema.from_orm(event).json())
        assert event_schema["start_date"] == data[0]["start_date"]

        response = await client.get(
            "/get_all",
            query=dict(
                maximum=100,
            ),
        )
        assert response.status_code == 200

        data = response.json().get("data")
        assert data[0]["title"] == "AsyncAdminAPIEvent_get_all"

        event_schema = json.loads(EventSchema.from_orm(event).json())
        assert event_schema["start_date"] == data[0]["start_date"]

        response = await client.get("/get_all")
        assert response.status_code == 200

        data = response.json().get("data")
        assert data[0]["title"] == "AsyncAdminAPIEvent_get_all"

        event_schema = json.loads(EventSchema.from_orm(event).json())
        assert event_schema["start_date"] == data[0]["start_date"]

    async def test_crud_default_get_delete(self, transactional_db, easy_api_client):
        client = easy_api_client(AutoGenCrudAPIController)

        object_data = dummy_data.copy()
        object_data.update(title=f"{object_data['title']}_get")

        event = await sync_to_async(Event.objects.create)(**object_data)

        response = await client.get(
            f"/?pk={event.id}",
        )
        assert response.status_code == 200

        data = response.json().get("data")
        assert data["title"] == "AsyncAdminAPIEvent_get"

        event_schema = json.loads(EventSchema.from_orm(event).json())
        assert event_schema["end_date"] == data["end_date"]

        await client.delete(
            f"/?pk={event.id}",
        )

        response = await client.get(
            f"/?pk={event.id}",
        )
        assert response.status_code == 200
        assert response.json().get("code") == 404

    async def test_crud_default_create(self, transactional_db, easy_api_client):
        client = easy_api_client(AutoGenCrudAPIController)

        client_c = await sync_to_async(Client.objects.create)(
            name="Client C for Unit Testings", key="C"
        )

        client_d = await sync_to_async(Client.objects.create)(
            name="Client D for Unit Testings", key="D"
        )

        type = await sync_to_async(Type.objects.create)(name="TypeForCreating")

        object_data = dummy_data.copy()
        object_data.update(title=f"{object_data['title']}_create")
        object_data.update(owner=[client_c.id, client_d.id])
        object_data.update(lead_owner=[client_d.id])
        object_data.update(type_id=type.id)

        response = await client.put(
            "/", json=object_data, content_type="application/json"
        )
        assert response.status_code == 200

        assert response.json().get("code") == 201
        event_id = response.json().get("data")["id"]

        response = await client.get(
            f"/?pk={event_id}",
        )
        assert response.status_code == 200
        assert response.json().get("data")["title"] == "AsyncAdminAPIEvent_create"

    async def test_crud_default_create_some_fields(
        self, transactional_db, easy_api_client
    ):
        client = easy_api_client(AutoGenCrudSomeFieldsAPIController)

        client_type = await sync_to_async(Client.objects.create)(
            name="Client for Unit Testings",
            key="Type",
            category=None,
            password="DUMMY_PASSWORD",
        )

        response = await client.get(
            f"/?pk={client_type.id}",
        )
        assert response.status_code == 200
        assert response.json()["data"]["key"] == "Type"

    async def test_crud_default_patch(self, transactional_db, easy_api_client):
        client = easy_api_client(AutoGenCrudAPIController)

        object_data = dummy_data.copy()
        event = await sync_to_async(Event.objects.create)(**object_data)

        response = await client.get(
            f"/?pk={event.pk}",
        )
        assert response.status_code == 200
        assert response.json().get("data")["title"] == f"{object_data['title']}"

        client_e = await sync_to_async(Client.objects.create)(
            name="Client E for Unit Testings", key="E"
        )

        client_f = await sync_to_async(Client.objects.create)(
            name="Client F for Unit Testings", key="F"
        )

        new_data = dict(
            id=event.pk,
            title=f"{object_data['title']}_patch",
            start_date=str((datetime.now() + timedelta(days=10)).date()),
            end_date=str((datetime.now() + timedelta(days=20)).date()),
            owner=[client_e.pk, client_f.pk],
        )

        response = await client.patch(
            "/?pk=20000", json=new_data, content_type="application/json"
        )

        assert response.status_code == 200
        assert response.json()["code"] == 404

        response = await client.patch(
            f"/?pk={event.pk}", json=new_data, content_type="application/json"
        )

        assert response.status_code == 200
        assert response.json().get("data")["pk"] == event.pk

        response = await client.get(
            f"/?pk={event.pk}",
        )
        assert response.status_code == 200
        assert response.json().get("data")["title"] == "AsyncAdminAPIEvent_patch"
        assert response.json().get("data")["start_date"] == str(
            (datetime.now() + timedelta(days=10)).date()
        )
        assert response.json().get("data")["end_date"] == str(
            (datetime.now() + timedelta(days=20)).date()
        )

    async def test_default_filter(self, transactional_db, easy_api_client):
        object_data = dummy_data.copy()
        object_data.update(title=f"{object_data['title']}_filter")

        event = await sync_to_async(Event.objects.create)(**object_data)

        client = easy_api_client(AutoGenCrudAPIController)

        response = await client.get(
            "/filter", query=dict(filters=json.dumps(dict(id__gte=1)))
        )
        assert response.status_code == 200

        data = response.json().get("data")
        assert data[0]["title"] == "AsyncAdminAPIEvent_filter"

        event_schema = json.loads(EventSchema.from_orm(event).json())
        assert event_schema["end_date"] == data[0]["end_date"]

    async def test_crud_filter_exclude(self, transactional_db, easy_api_client):
        object_data = dummy_data.copy()
        object_data.update(title=f"{object_data['title']}_exclude")

        event = await sync_to_async(Event.objects.create)(**object_data)

        client = easy_api_client(AutoGenCrudAPIController)

        response = await client.get(
            "/filter_exclude", query=dict(filters=json.dumps(dict(id__lt=1)))
        )
        assert response.status_code == 200

        data = response.json().get("data")
        assert data[0]["title"] == "AsyncAdminAPIEvent_exclude"

        event_schema = json.loads(EventSchema.from_orm(event).json())
        assert event_schema["end_date"] == data[0]["end_date"]
