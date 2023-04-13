import datetime
import random

import allure
import pytest

from framework.testdata.users import MLSpaceUser
from framework.ui.pageobjects.mlspace.department_list_page import DepartmentListPage
from framework.ui.pageobjects.mlspace.project_list_page import ProjectListPage
from framework.ui.pageobjects.mlspace.project_page import ProjectPage


def generate_dep_name():
    return f'TestDep-{random.randint(99, 999)}-{datetime.datetime.now().date()}'


def generate_proj_name():
    return f'TestProj-{random.randint(99, 999)}'


@allure.label("Layer", "UI")
@allure.label("Type", "Auto")
@allure.feature("Проекты")
class TestProjects:

    @allure.title('Создание и удаление проекта')
    @pytest.mark.parametrize('product_user', [MLSpaceUser])
    def test_create_and_delete_project(self, browser):
        dep_name = generate_dep_name()
        proj_name = generate_proj_name()
        departments_page: DepartmentListPage = browser.navigate_to(DepartmentListPage)
        assert browser.is_page_current(DepartmentListPage)

        with allure.step("Создать департамент и проект"):
            departments_page.create(dep_name)
            assert departments_page.find_cell_by_name(dep_name).name() == dep_name

            departments_page.click_to_cell(dep_name)
            projects_page = ProjectListPage(browser.web_driver)
            assert projects_page.projects_empty_label.is_visible()

            projects_page.create(proj_name)
            projects_cell = projects_page.find_cell_by_name(proj_name)
            assert projects_cell.name() == proj_name
            assert projects_cell.department_name_label.text == dep_name

        with allure.step("Удалить проект и департамент"):
            projects_page.delete(proj_name)
            assert projects_page.projects_empty_label.is_visible()

            departments_page = browser.navigate_to(DepartmentListPage)
            dep_cell = departments_page.find_cell_by_name(dep_name)
            departments_page.delete(dep_name)
            assert dep_cell.name_label.is_not_visible()

    @allure.title('Добавление услуги в проект')
    @pytest.mark.parametrize('product_user', [MLSpaceUser])
    def test_add_service_to_project(self, browser):
        dep_name = generate_dep_name()
        proj_name = generate_proj_name()
        departments_page: DepartmentListPage = browser.navigate_to(DepartmentListPage)
        assert browser.is_page_current(DepartmentListPage)

        with allure.step("Создать департамент и проект"):
            departments_page.create(dep_name)
            assert departments_page.find_cell_by_name(dep_name).name() == dep_name

            departments_page.click_to_cell(dep_name)
            projects_page = ProjectListPage(browser.web_driver)
            assert projects_page.projects_empty_label.is_visible()

            projects_page.create(proj_name)
            projects_cell = projects_page.find_cell_by_name(proj_name)
            assert projects_cell.name() == proj_name
            assert projects_cell.department_name_label.text == dep_name

        with allure.step("Добавить услугу в MlSpace"):
            projects_page.click_to_cell(cell=projects_cell)
            project_page = ProjectPage(browser.web_driver)
            project_page.add_mlspace_service()
            card = project_page.mlspace_card
            assert card.status() == 'услуга активна'
            assert card.activation_date() == datetime.datetime.now().date()

        with allure.step("Проверить что консоль открывается"):
            card.open_console_button.click()
            browser.switch_to_tab(1)
            assert browser.is_url_include_str('mlspace.poc.ai.4cloud.cf/')
