from MobileInventory import MobileInventory, InsufficientException
import pytest

class TestingInventoryCreation():
    def test_creating_empty_inventory(self):
        object = MobileInventory({})
    def test_creating_specified_inventory(self):
        object = MobileInventory({})
        object.add_stock({'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
        #object.print_data()
    def test_creating_inventory_with_list(self):
        with pytest.raises(TypeError):
            object = MobileInventory(['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'])
    def test_creating_inventory_with_numeric_keys(self):
        with pytest.raises(ValueError):
            object = MobileInventory({1: 'iPhone Model X', 2: 'Xiaomi Model Y', 3: 'Nokia Model Z'})
    def test_creating_inventory_with_nonnumeric_values(self):
        with pytest.raises(ValueError):
            object = MobileInventory({'iPhone Model X': '100', 'Xiaomi Model Y': '1000', 'Nokia Model Z': '25'})
    def test_creating_inventory_with_negative_value(self):
        with pytest.raises(ValueError):
            object = MobileInventory({'iPhone Model X': -45, 'Xiaomi Model Y': 200, 'Nokia Model Z': 25})

class TestInventoryAddStock():

    @pytest.fixture(scope='module')
    def setup_class(self):
        self.inventory = MobileInventory({'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
        return self.inventory
    def test_add_new_stock_as_dict(self, setup_class):
        setup_class.add_stock({'iPhone Model X':50, 'Xiaomi Model Y': 2000, 'Nokia Model A':10})
        assert setup_class.balance_inventory == {'iPhone Model X':150, 'Xiaomi Model Y': 3000, 'Nokia Model Z':25, 'Nokia Model A':10}
    def test_add_new_stock_as_list(self, setup_class):
        with pytest.raises(TypeError):
            setup_class.add_stock(['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'])
    def test_add_new_stock_with_numeric_keys(self, setup_class):
        with pytest.raises(ValueError):
            setup_class.add_stock({1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'})
    def test_add_new_stock_with_nonnumeric_values(self, setup_class):
        with pytest.raises(ValueError):
            setup_class.add_stock({'iPhone Model A':'50', 'Xiaomi Model B':'2000', 'Nokia Model C':'25'})
    def test_add_new_stock_with_float_values(self, setup_class):
        with pytest.raises(ValueError):
            setup_class.add_stock({'iPhone Model A':50.5, 'Xiaomi Model B':2000.3, 'Nokia Model C':25})

class TestInventorySellStock():
    @pytest.fixture(scope='module')
    def setup_class(self):
        self.inventory = MobileInventory({'iPhone Model A':50, 'Xiaomi Model B': 2000, 'Nokia Model C':10, 'Sony Model D':1})
        return self.inventory
    def test_sell_stock_as_dict(self, setup_class):
        setup_class.sell_stock({'iPhone Model A':2, 'Xiaomi Model B':20, 'Sony Model D':1})
        assert setup_class.balance_inventory == {'iPhone Model A':48, 'Xiaomi Model B': 1980, 'Nokia Model C':10, 'Sony Model D':0}
    def test_sell_stock_as_list(self, setup_class):
        with pytest.raises(TypeError):
            setup_class.sell_stock(['iPhone Model A', 'Xiaomi Model B', 'Nokia Model C'])
    def test_sell_stock_with_numeric_keys(self, setup_class):
        with pytest.raises(ValueError):
            setup_class.sell_stock({1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'})
    def test_sell_stock_with_nonnumeric_values(self, setup_class):
        with pytest.raises(ValueError):
            setup_class.sell_stock({'iPhone Model A':'2', 'Xiaomi Model B':'3', 'Nokia Model C':'4'})
    def test_sell_stock_with_float_values(self, setup_class):
        with pytest.raises(ValueError):
            setup_class.sell_stock({'iPhone Model A':2.5, 'Xiaomi Model B':3.1, 'Nokia Model C':4})
    def test_sell_stock_of_nonexisting_model(self, setup_class):
        with pytest.raises(InsufficientException):
            setup_class.sell_stock({'iPhone Model B':2, 'Xiaomi Model B':5})
    def test_sell_stock_of_insufficient_stock(self, setup_class):
        with pytest.raises(InsufficientException):
            setup_class.sell_stock({'iPhone Model A':2, 'Xiaomi Model B':5, 'Nokia Model C': 15})

