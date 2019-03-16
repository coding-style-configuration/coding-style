from bddrest import response, when, status, given

from coding-style.models import Foo
from coding-style.tests.helpers import LocalApplicationTestCase


class TestFoo(LocalApplicationTestCase):

    @classmethod
    def mockup(cls):
        session = cls.create_session()

        # Adding 5 Foos
        for i in range(5):
            session.add(Foo(title=f'Foo {i}'))

        session.commit()

    def test_foo_crud(self):
 
        # Creating a new Foo!
        with self.given(
            'Create a new Foo',
            '/apiv1/foos',
            'CREATE',
            form=dict(title='First foo')
        ):
            assert status == 200
            assert 'title' in response.json
            assert response.json['title'] == 'First foo'
            assert response.json['createdAt'] is not None
            assert response.json['modifiedAt'] is None
            foo_id = response.json['id']

            # Edit it!
            when(
                'Updating the title',
                f'/apiv1/foos/id: {foo_id}',
                'EDIT',
                form=given | dict(title='First foo(edited)')
            )
            assert status == 200
            assert response.json['title'] == 'First foo(edited)'
            assert response.json['modifiedAt'] is not None

            # Get it!
            when(
                'Retrieve the first foo',
                f'/apiv1/foos/id: {foo_id}',
                'GET',
                form=None,
            )
            assert status == 200
            assert response.json['title'] == 'First foo(edited)'
            assert response.json['id'] == foo_id

            # Delete it!
            when(
                'Removing the first foo',
                f'/apiv1/foos/id: {foo_id}',
                'DELETE',
                form=None
            )
            assert status == 200
            assert response.json['title'] == 'First foo(edited)'
            assert response.json['id'] == foo_id

            # Get it again to ensure it removed
            when(
                'Retrieve the first foo',
                f'/apiv1/foos/id: {foo_id}',
                'GET',
                form=None,
            )
            assert status == 404

    def test_foo_list(self):

        # Listing all foos
        with self.given(
            'Listing all Foos',
            '/apiv1/foos',
            'LIST',
        ):
            assert status == 200
            assert len(response.json) >= 5

            when(
                'Paginating',
                query=dict(take=1, skip=2, sort='id')
            )
            assert status == 200
            assert len(response.json) == 1
            assert response.json[0]['title'] == 'Foo 2'

