from framework.helpers.wait import wait_while
from framework.ui.core.primitive_elements.base_element import BaseElement
from framework.ui.core.primitive_elements.button import Button
from framework.ui.core.primitive_elements.grid_cell import GridCell
from framework.ui.core.primitive_elements.label import Label
from framework.ui.core.wrappers.locator import Locator
from framework.ui.pageelements.mlspace.department_delete_form import DepartmentDeleteForm
from framework.ui.pageelements.mlspace.project_cell import ProjectCell
from framework.ui.pageelements.mlspace.project_creating_form import ProjectCreatingForm
from framework.ui.pageobjects.base_page import BasePage


class ProjectListPage(BasePage):
    """ Страница со списком проектов """

    def __init__(self, web_driver):
        self.web_driver = web_driver

    @property
    def page_path(self):
        return "/organization/departments/departments/view/{id}"

    @property
    def create_project_button(self) -> Button:
        return Button(self.web_driver, Locator.xpath('//button[starts-with(@class, "AddSerivce-0_0_0-a1smk7ax")]'))

    @property
    def name_label(self) -> Label:
        return Label(self.web_driver, Locator.xpath('//div[@class="Title-0_0_0-tkrdwj8"]'))

    @property
    def description_label(self) -> Label:
        return Label(self.web_driver, Locator.xpath('//div[@class="Description-0_0_0-d1xigkqd"]'))

    @property
    def admin_name_label(self) -> Label:
        return Label(self.web_driver, Locator.xpath('//div[@class="Name-0_0_0-n13qt1zm"]'))

    @property
    def limit_label(self) -> Label:
        return Label(self.web_driver, Locator.xpath('//div[@class="Value-0_0_0-v5l0nbx"]'))

    @property
    def projects_empty_label(self) -> Label:
        return Label(self.web_driver, Locator.xpath('//div[@class="Content-0_0_0-c1j5p54g"]'))

    @property
    def project_creating_form(self) -> ProjectCreatingForm:
        form = BaseElement(self.web_driver, Locator.xpath('//form/div[@class="Wrapper-0_0_0-wesrq5v"]'))
        if not form.is_visible():
            raise Exception(f"Project creating form not found. Locator: {form.locator}")
        return ProjectCreatingForm(form.element)

    @property
    def delete_form(self) -> DepartmentDeleteForm:
        delete_form = BaseElement(self.web_driver, Locator.xpath('//form/div[@class="Wrapper-0_0_0-wesrq5v"]'))
        if not delete_form.is_visible():
            raise Exception(f"Department deleting form not found. Locator: {delete_form.locator}")
        return DepartmentDeleteForm(delete_form.element)

    def find_cell_by_name(self, name: str) -> ProjectCell:
        grid = BaseElement(self.web_driver, Locator.xpath('//div[@class="Grid-0_0_0-g1pzgd74"]'))
        if not grid.is_visible():
            raise Exception(f"Project cells grid not found. Locator: {grid.locator}")

        cell_list = GridCell(grid.element, Locator.xpath('.//div[starts-with(@class,"Wrapper-0_0_0-w1z0o8fe")]'))
        if not cell_list.is_visible():
            raise Exception(f"Project cell not found. Locator: {cell_list.locator}")

        def find_cell():
            for el in cell_list.element_list:
                project = ProjectCell(el)
                if project.name_label.is_visible() and project.name() == name:
                    return project

        return wait_while(find_cell)

    def create(self, name: str, description: str = None):
        self.create_project_button.click()
        form = self.project_creating_form
        form.project_name_field.fill(name)
        if description:
            form.description_field.fill(description)
        form.create_button.click()

    def delete(self, name: str):
        project_cell = self.find_cell_by_name(name)
        project_cell.delete_menu_button.click()
        project_cell.delete_button.click()

        self.delete_form.delete_button.click()

    def click_to_cell(self, name: str = None, cell: ProjectCell = None):
        if name:
            self.find_cell_by_name(name).base_element.click()
            return
        if cell:
            cell.base_element.click()
