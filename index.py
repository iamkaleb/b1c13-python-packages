from appliances import DishWasher, Refrigerator, CanOpener, CoffeeMaker, Stove, Dryer, Washer

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

cutco_opener = CanOpener("Maroon")
cutco_opener.open_can()