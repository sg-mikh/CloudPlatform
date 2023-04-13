from framework.helpers.wait import wait_while
from framework.ui.core.primitive_elements.base_element import BaseElement
from framework.ui.core.primitive_elements.button import Button
from framework.ui.core.primitive_elements.grid_cell import GridCell
from framework.ui.core.primitive_elements.label import Label
from framework.ui.core.wrappers.locator import Locator
from framework.ui.pageelements.mlspace.department_cell import DepartmentCell
from framework.ui.pageelements.mlspace.department_create_form import DepartmentCreateForm
from framework.ui.pageelements.mlspace.department_delete_form import DepartmentDeleteForm
from framework.ui.pageelements.mlspace.error_on_delete_form import ErrorOnDeleteForm
from framework.ui.pageobjects.base_page import BasePage


class DepartmentListPage(BasePage):

    def __init__(self, web_driver):
        self.web_driver = web_driver

    @property
    def page_path(self):
        return "/organization/departments"

    @property
    def create_button(self) -> Button:
        return Button(self.web_driver, Locator.xpath('//button[starts-with(@class, "AddDepartment")]'))

    @property
    def impossible_delete_label(self) -> Label:
        return Label(self.web_driver, Locator.xpath('//form/.//div[contains(text(), "Невозможно удалить")]'))

    @property
    def creating_form(self) -> DepartmentCreateForm:
        creating_form = BaseElement(self.web_driver, Locator.xpath('//form/div[@class="Wrapper-0_0_0-wesrq5v"]'))
        if not creating_form.is_visible():
            raise Exception(f"Department creating form not found. Locator: {creating_form.locator}")
        return DepartmentCreateForm(creating_form.element)

    @property
    def delete_form(self) -> DepartmentDeleteForm:
        delete_form = BaseElement(self.web_driver, Locator.xpath('//form/div[@class="Wrapper-0_0_0-wesrq5v"]'))
        if not delete_form.is_visible():
            raise Exception(f"Department deleting form not found. Locator: {delete_form.locator}")
        return DepartmentDeleteForm(delete_form.element)

    @property
    def error_on_delete_form(self):
        form = BaseElement(self.web_driver, Locator.xpath('//form/div[@class="Wrapper-0_0_0-wesrq5v"]'))
        if not form.is_visible():
            raise Exception(f"Error form not found. Locator: {form.locator}")
        return ErrorOnDeleteForm(form.element)

    def find_cell_by_name(self, name: str) -> DepartmentCell:
        grid = BaseElement(self.web_driver, Locator.xpath('//div[@class="Grid-0_0_0-gp2mgi7"]'))
        if not grid.is_visible():
            raise Exception(f"Department cells grid not found. Locator: {grid.locator}")

        cell_list = GridCell(grid.element, Locator.xpath('.//div[starts-with(@class,"Wrapper-0_0_0-w1mhuvnq")]'))
        if not cell_list.is_visible():
            raise Exception(f"Department cell not found. Locator: {cell_list.locator}")

        def find_cell():
            for el in cell_list.element_list:
                dep_tile = DepartmentCell(el)
                if dep_tile.name_label.is_visible() and dep_tile.name() == name:
                    return dep_tile

        return wait_while(find_cell)

    def click_to_cell(self, name: str):
        el = self.find_cell_by_name(name)
        el.base_element.click()

    def create(self, name: str, description: str = None):
        self.create_button.click()
        creating_form = self.creating_form
        creating_form.name_input.fill(name)
        if description:
            creating_form.description_input.fill(description)
        creating_form.create_button.click()

    def delete(self, name: str):
        department_cell = self.find_cell_by_name(name)
        department_cell.delete()
        self.delete_form.delete_button.click()
