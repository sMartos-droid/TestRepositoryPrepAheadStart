from srcFiles.employee import Employee
import pytest


@pytest.mark.parametrize(
    "testInput, expectedEmployeeID",
    [
        (Employee("John", "Doe", 78035946, 1300, "junior", 35000), 1300),
        (Employee("Jane", "Smith", 78035947, 1, "senior", 60000), 1),
        (Employee("Bob", "Johnson", 78035948, 2, "manager", 70000), 2),
        (Employee("Allan", "Dunn", 78035950, 3, "director", 80000), 3),
    ],
)
def test_getEmployeeID(testInput, expectedEmployeeID):
    assert testInput.getEmployeeID() == expectedEmployeeID


@pytest.mark.parametrize(
    "testInput, expectedGrade",
    [
        (Employee("John", "Doe", 78035946, 1300, "junior", 35000), "juni"),
        (Employee("Jane", "Smith", 78035947, 1, "senior", 60000), "senior"),
        (Employee("Bob", "Johnson", 78035948, 2, "manager", 70000), "manager"),
        (Employee("Allan", "Dunn", 78035950, 3, "director", 80000), "director"),
    ],
)
def test_getGrade(testInput, expectedGrade):
    assert testInput.getGrade() == expectedGrade


@pytest.mark.parametrize(
    "testInput, expectedSalary",
    [
        (Employee("John", "Doe", 78035946, 1300, "junior", 35000), 35000),
        (Employee("Jane", "Smith", 78035947, 1, "senior", 60000), 60000),
        (Employee("Bob", "Johnson", 78035948, 2, "manager", 70000), 70000),
        (Employee("Allan", "Dunn", 78035950, 3, "director", 80000), 80000),
    ],
)
def test_getSalary(testInput, expectedSalary):
    assert testInput.getSalary() == expectedSalary


@pytest.mark.parametrize(
    "testInput, newEmployeeID",
    [
        (Employee("John", "Doe", 78035946, 1300, "junior", 35000), 1301),
        (Employee("Jane", "Smith", 78035947, 1, "senior", 60000), 2),
        (Employee("Bob", "Johnson", 78035948, 2, "manager", 70000), 3),
        (Employee("Allan", "Dunn", 78035950, 3, "director", 80000), 4),
    ],
)
def test_setEmployeeID(testInput, newEmployeeID):
    testInput.setEmployeeID(newEmployeeID)
    assert testInput.getEmployeeID() == newEmployeeID


@pytest.mark.parametrize(
    "testInput, newGrade",
    [
        (Employee("John", "Doe", 78035946, 1300, "junior", 35000), "senior"),
        (Employee("Jane", "Smith", 78035947, 1, "senior", 60000), "junior"),
        (Employee("Bob", "Johnson", 78035948, 2, "manager", 70000), "director"),
        (Employee("Allan", "Dunn", 78035950, 3, "director", 80000), "manager"),
    ],
)
def test_setGrade(testInput, newGrade):
    testInput.setGrade(newGrade)
    assert testInput.getGrade() == newGrade
