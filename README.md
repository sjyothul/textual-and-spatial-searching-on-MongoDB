# textual-and-spatial-searching-on-MongoDB
textual and spatial searching on MongoDB

FindBusinessBasedOnCity(cityToSearch, minReviewCount, saveLocation1, collection)
This function searches the ‘collection’ given to find all the business present in the city provided in ‘cityToSearch’ and have at least ‘review_count’ of minReviewCount and save it to ‘saveLocation1’. For each business you found, you should store name Full address, city, state of business in the following format. Each line of the saved file will contain, Name$FullAddress$City$State$Stars. ($ is the separator and must be present)

FindBusinessBasedOnLocation(categoriesToSearch, myLocation, minDistance, maxDistance, saveLocation2, collection)
This function searches the ‘collection’ given to find name of all the business present in the ‘maxDistance’ from the given ‘myLocation’ that covers all the given categories (the business category needs to match at least one of the given categories) (please use the distance algorithm given below) and save them to ‘saveLocation2’. Each line of the output file will contain the name of the business only.
-- categoriesToSearch: a list of categories need to be covered
-- ‘myLocation’ will be given with format [“40.3”, “51.6”].
-- minDistance and maxDistance: the search range distance
-- saveLocation2: output location
