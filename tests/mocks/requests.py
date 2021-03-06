from datetime import datetime
from pytest import fixture
from models import Request
from models.request import ProductArea


@fixture(scope='function')
def valid_request_model(valid_client_model, valid_staff_model):
    """
    A fixture for creating a valid request model.

    Args:
        valid_client_model (Model): a valid client model created by a fixture.
        valid_staff_model (Model): a valid staff model created by a fixture.
    """
    return Request(
        title='Improve customer care services',
        description='The current customer care services are reported to '
        'be abysmal with representatives dropping calls on customer or '
        'being rather unpleasant.',
        product_area=ProductArea.POLICIES,
        target_date=datetime.utcnow(),
        priority=1,
        staff_id=1,
        client_id=1,
    ).save()


@fixture(scope='function')
def valid_request_model_no_save(valid_client_model, valid_staff_model):
    """
    A fixture for creating a valid request model without saving it to the db.

    Args:
        valid_client_model (Model): a valid client model created by a fixture.
        valid_staff_model (Model): a valid staff model created by a fixture.
    """
    return Request(
        title='Improve customer care services',
        description='The current customer care services are reported to '
        'be abysmal with representatives dropping calls on customer or '
        'being rather unpleasant.',
        product_area=ProductArea.POLICIES,
        target_date=datetime.utcnow(),
        priority=1,
        staff_id=1,
        client_id=1,
    )


@fixture(scope='function')
def multiple_valid_request_models(
    multiple_valid_client_models, multiple_valid_staff_models
):
    """
    A fixture for creating a multiple valid requests.

    Args:
        multiple_valid_client_models (list): a list of valid client models
            created by a fixture.
        multiple_valid_staff_models (list): a list of valid staff models
            created by a fixture.
    """
    requests = [
        Request(
            title='Improve customer care services',
            description='The current customer care services are reported to '
            'be abysmal with representatives dropping calls on customer or '
            'being rather unpleasant.',
            product_area=ProductArea.POLICIES,
            target_date=datetime.utcnow(),
            priority=i,
            staff_id=1,
            client_id=1,
        ).save() for i in range(12)
    ]

    return requests


@fixture(scope='function')
def valid_request_body(valid_client_model, valid_staff_model):
    """
    A fixture for creating a valid request body.

    Args:
        valid_client_model (Model): a valid client model created by a fixture.
        valid_staff_model (Model): a valid staff model created by a fixture.
    """
    return {
        'title': 'Improve customer care services',
        'description':
            'The current customer care services are reported to '
            'be abysmal with representatives dropping calls on customer or '
            'being rather unpleasant.',
        'product_area': 'POLICIES',
        'target_date': '2019-10-05T00:00:00Z',
        'priority': 1,
        'staff_id': 1,
        'client_id': 1,
    }


@fixture(scope='function')
def valid_request_body_with_existing_priority(valid_request_model):
    """
    A fixture for creating a request body with existing priority number
    for a client.

    Args:
        valid_request_model (Model): a valid request model created by a
            fixture.
    """
    return {
        'title': 'Add PayPal payment support',
        'description':
            'Client B wants to be able to purchase using '
            'his PayPal',
        'product_area': 'BILLING',
        'target_date': '2019-10-05T00:00:00Z',
        'priority': 1,
        'staff_id': 1,
        'client_id': 1,
    }


@fixture(scope='function')
def invalid_request_body_with_missing_fields(
    valid_client_model, valid_staff_model
):
    """
    A fixture for creating a request body with missing fields.

    Args:
        valid_client_model (Model): a valid client model created by a fixture.
        valid_staff_model (Model): a valid staff model created by a fixture.
    """
    return {
        'title': 'Improve customer care services',
        'description':
            'The current customer care services are reported to '
            'be abysmal with representatives dropping calls on customer or '
            'being rather unpleasant.',
        'product_area': 'POLICIES',
        'target_date': '2019-10-05T00:00:00Z',
        'priority': 1,
    }


@fixture(scope='function')
def invalid_request_body_with_non_existent_client(valid_staff_model):
    """
    A fixture for creating a request body with non-existent client id.

    Args:
        valid_staff_model (Model): a valid staff model created by a fixture.
    """
    return {
        'title': 'Improve customer care services',
        'description':
            'The current customer care services are reported to '
            'be abysmal with representatives dropping calls on customer or '
            'being rather unpleasant.',
        'product_area': 'POLICIES',
        'target_date': '2019-10-05T00:00:00Z',
        'priority': 1,
        'staff_id': 1,
        'client_id': 1,
    }


@fixture(scope='function')
def invalid_request_body_with_non_existent_staff(valid_client_model):
    """
    A fixture for creating a request body with non-existent staff id.

    Args:
        valid_client_model (Model): a valid client model created by a fixture.
    """
    return {
        'title': 'Improve customer care services',
        'description':
            'The current customer care services are reported to '
            'be abysmal with representatives dropping calls on customer or '
            'being rather unpleasant.',
        'product_area': 'POLICIES',
        'target_date': '2019-10-05T00:00:00Z',
        'priority': 1,
        'staff_id': 1,
        'client_id': 1,
    }


@fixture(scope='function')
def invalid_request_body_with_invalid_enum_value(
    valid_client_model, valid_staff_model
):
    """
    A fixture for creating a request body with invalid enum value.

    Args:
        valid_client_model (Model): a valid client model created by a fixture.
        valid_staff_model (Model): a valid staff model created by a fixture.
    """
    return {
        'title': 'Improve customer care services',
        'description':
            'The current customer care services are reported to '
            'be abysmal with representatives dropping calls on customer or '
            'being rather unpleasant.',
        'product_area': 'POLITICS',
        'target_date': '2019-10-05T00:00:00Z',
        'priority': 1,
        'staff_id': 1,
        'client_id': 1,
    }


@fixture(scope='function')
def invalid_request_body_with_invalid_string_length(
    valid_client_model, valid_staff_model
):
    """
    A fixture for creating a request body with invalid string length.

    Args:
        valid_client_model (Model): a valid client model created by a fixture.
        valid_staff_model (Model): a valid staff model created by a fixture.
    """
    return {
        'title': 'Improve customer care services',
        'description':
            'The current customer care services are reported to '
            'be abysmal with representatives dropping calls on customer or '
            'being rather unpleasant. We need to do something about this and '
            'more importantly we need to make an example. This is not '
            'allowed. This should never be allowed and that\'s all I have to '
            'say on the matter. Thanks. Yours faithfully,',
        'product_area': 'POLICIES',
        'target_date': '2019-10-05T00:00:00Z',
        'priority': 1,
        'staff_id': 1,
        'client_id': 1,
    }


@fixture(scope='function')
def invalid_request_body_with_invalid_priority(
    valid_client_model, valid_staff_model
):
    """
    A fixture for creating a request body with invalid priority.

    Args:
        valid_client_model (Model): a valid client model created by a fixture.
        valid_staff_model (Model): a valid staff model created by a fixture.
    """
    return {
        'title': 'Improve customer care services',
        'description':
            'The current customer care services are reported to '
            'be abysmal with representatives dropping calls on customer or '
            'being rather unpleasant.',
        'product_area': 'POLICIES',
        'target_date': '2019-10-05T00:00:00Z',
        'priority': 100,
        'staff_id': 1,
        'client_id': 1,
    }


@fixture(scope='function')
def bad_request_json_string(valid_client_model, valid_staff_model):
    """
    A fixture for creating a bad request body.

    Args:
        valid_client_model (Model): a valid client model created by a fixture.
        valid_staff_model (Model): a valid staff model created by a fixture.
    """
    # Json string contains an extra comma.
    return (
        """
        {
            "title": "Improve customer care services",
            "description": "The current customer care services are reported.",
            "product_area": "POLICIES",
            "target_date": "2019-10-05T00:00:00Z",
            "priority": 1,
            "staff_id": 1,
            "client_id": 1,
        }
        """
    )


@fixture(scope='function')
def invalid_request_body_with_invalid_date(
    valid_client_model, valid_staff_model
):
    """
    A fixture for creating a request body with invalid date.

    Args:
        valid_client_model (Model): a valid client model created by a fixture.
        valid_staff_model (Model): a valid staff model created by a fixture.
    """
    return {
        'title': 'Improve customer care services',
        'description':
            'The current customer care services are reported to '
            'be abysmal with representatives dropping calls on customer or '
            'being rather unpleasant.',
        'product_area': 'POLICIES',
        'target_date': '2019-03-05T00:00:00Z',
        'priority': 1,
        'staff_id': 1,
        'client_id': 1,
    }
