import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')

    assert user ['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')

    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')

    assert r['total_count'] == 58   
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('natashasadova')

    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')

    assert r['total_count'] != 0


@pytest.mark.api
def test_open_list_repositories_for_a_user(github_api):
    r = github_api.list_repositories_for_a_user('NataliiaSadova')

    assert (len(r)) == 2


@pytest.mark.api
def test_open_list_repositories_for_a_non_existing_user(github_api):
    r = github_api.list_repositories_for_a_user('NatashaSadova')
    
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_open_list_of_existing_users(github_api):
    users_id = 45
    r = github_api.list_users(users_id)
    
    assert len(r) != 0


@pytest.mark.api
def test_open_list_of_non_existing_users(github_api):
    id_no_existe = 999999999
    r = github_api.list_users(id_no_existe)
    
    assert len(r) == 0

