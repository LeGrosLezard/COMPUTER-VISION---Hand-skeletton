#
from recuperate_features import data_informations
#
from recuperate_features import passation_informations
#
from knn import recuperate_minimal_informations
#
from convert_variable import element_to_dict
#
from recuperate_points_to_search import searching_points
#
from built_points import modify_points




def less_one_points_detected(informations1):

    """Here we need to run our csv data for find points
    who's corresponding to our none detected points passation.
    If we found points we reconstruct the hand skeletton."""

    #Data needed
    distance_list, angulus_list, scale_list,\
    pts, angulus, distances, scale, finger_name, data, points = informations1


    #Run points into the finger
    for nb, i in enumerate(pts):

        if i == ((0, 0), (0, 0)):   #No detection of points

            print("phax :", nb)

            #Recuperate distance/angulus with the minimal distance of our passation
            a, b = recuperate_minimal_informations(distance_list, angulus_list, scale_list,
                                                    pts, angulus, distances, scale, finger_name)
            dist_index, angulus_index = a, b
            print(dist_index, angulus_index)

            #Data needed for re built our passation points
            first_part = (data, dist_index, angulus_index, distance_list,
                          angulus_list, finger_name, pts)

            #Rebuilt points
            points = modify_points(first_part, points, finger_name, nb, pts)


    return points



def reconstruction_points(points, scale):
    """1) - Here we run our skeletton points.
       2) - We order/annotated finger's into dictionnary
       3) - Run data csv
       4) - Make a knn for find data closer to our passation points
       5) - re built points."""



    """ONE) - Data treatment"""

    #Passation treatment.
    angulus, distances, scale = passation_informations(points, scale)

    #Data treatment.
    distance_list, angulus_list, scale_list, data = data_informations()

    #Passatation data to dictionnary. Annotations of fingers.
    angulus = element_to_dict(angulus)
    distances = element_to_dict(distances)
    points = element_to_dict(points)

    #Search point none detected.
    to_search = searching_points(points)
    print(to_search, "\n")



    """TWO) - Compare data with passation"""

    for finger_name, pts in to_search.items():


        """TWO A) - Less one point detected. Can rebuilt finger"""
        if pts != []:
            print(finger_name)

            informations1 = (distance_list, angulus_list, scale_list,
                             pts, angulus, distances, scale, finger_name, data, points)

            points = less_one_points_detected(informations1)


        """TWO B) - Finger no detected."""
        elif pts == []:
            pass


    print(points)




 


if __name__ == "__main__":



    points = [((0, 0), (0, 0)), ((97, 105), (115, 94)), ((115, 94), (122, 79)), ((122, 79), (126, 69)), ((0, 0), (0, 0)), ((86, 76), (83, 55)), ((83, 55), (83, 47)), ((83, 47), (83, 40)), ((0, 0), (0, 0)), ((75, 79), (68, 55)), ((0, 0), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (0, 0)), ((51, 98), (44, 91)), ((44, 91), (40, 94)), ((40, 94), (41, 90))]
    scale = (31, 31, 113, 109)

    #points = [((0, 0), (0, 0)), ((120, 153), (147, 132)), ((147, 132), (158, 104)), ((158, 104), (169, 83)), ((93, 170), (99, 105)), ((99, 105), (110, 78)), ((110, 78), (132, 62)), ((132, 62), (83, 61)), ((93, 170), (83, 110)), ((83, 110), (50, 100)), ((50, 100), (24, 93)), ((24, 93), (152, 45)), ((93, 170), (77, 126)), ((77, 126), (50, 121)), ((50, 121), (29, 115)), ((29, 115), (126, 45)), ((93, 170), (77, 137)), ((77, 137), (56, 143)), ((56, 143), (45, 137)), ((45, 137), (35, 132))]
    #scale = (3, 17, 194, 214)


    reconstruction_points(points, scale)






