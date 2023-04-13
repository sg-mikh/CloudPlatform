import datetime
import random

import allure
import pytest

from framework.testdata.users import MLSpaceUser
from framework.ui.pageobjects.mlspace.department_list_page import DepartmentListPage
from framework.ui.pageobjects.mlspace.project_list_page import ProjectListPage


def generate_dep_name():
    return f'TestDep-{random.randint(99, 999)}-{datetime.datetime.now().date()}'


def generate_proj_name():
    return f'TestProj-{random.randint(99, 999)}'


@allure.label("Layer", "UI")
@allure.label("Type", "Auto")
@allure.feature("Департаменты")
class TestDepartments:

    @allure.title("Создание и удаление департамента")
    @pytest.mark.parametrize('product_user', [MLSpaceUser])
    def test_create_new_and_delete(self, browser):
        name = generate_dep_name()
        departments_page: DepartmentListPage = browser.navigate_to(DepartmentListPage)
        assert browser.is_page_current(DepartmentListPage)

        with allure.step("Создать департамент"):
            departments_page.create(name)
            department_cell = departments_page.find_cell_by_name(name)
            assert department_cell.name() == name

        with allure.step("Удалить департамент"):
            departments_page.delete(name)
            assert department_cell.name_label.is_not_visible()

    @allure.title("Создание и удаление департамента с проектом")
    @pytest.mark.parametrize('product_user', [MLSpaceUser])
    def test_create_new_and_delete_with_project(self, browser):
        dep_name = generate_dep_name()
        proj_name = generate_proj_name()
        departments_page: DepartmentListPage = browser.navigate_to(DepartmentListPage)
        assert browser.is_page_current(DepartmentListPage)

        with allure.step("Создать департамент"):
            departments_page.create(dep_name)
            assert departments_page.find_cell_by_name(dep_name).name() == dep_name

        with allure.step("Создать проект"):
            departments_page.click_to_cell(dep_name)
            projects_page = ProjectListPage(browser.web_driver)
            assert projects_page.projects_empty_label.is_visible()

            projects_page.create(proj_name)
            projects_cell = projects_page.find_cell_by_name(proj_name)
            assert projects_cell.name() == proj_name
            assert projects_cell.department_name_label.text == dep_name

        with allure.step("Проверить что департамент не удаляется"):
            departments_page = browser.navigate_to(DepartmentListPage)
            departments_page.find_cell_by_name(dep_name).delete()
            assert departments_page.error_on_delete_form.ok_button.is_visible()
