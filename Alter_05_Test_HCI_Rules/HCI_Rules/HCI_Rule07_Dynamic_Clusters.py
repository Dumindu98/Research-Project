import base64
import collections
import math
import base64
import collections
from io import BytesIO
from operator import itemgetter

import numpy as np
from PIL import Image
from skimage import util


class HCI_Rule:
    def __init__(self, imageName):
        self.imageName = imageName

    def run(self):
        imgPath = 'Alter_Backend/Alter_05_Test_HCI_Rules/generated_web_ui/'.__add__(self.imageName)
        img = Image.open(imgPath)
        img = np.array(img)
        img = util.img_as_ubyte(img)
        img = img.reshape(-1, 3)
        img = [tuple(l) for l in img]
        hist = collections.Counter(img)
        hist = hist.items()
        frequency = []

        # Create list from histogram
        for x in hist:
            add = x[0][0], x[0][1], x[0][2], x[1]
            frequency.append(add)

        # Sort the pixels on frequency. This way we can cut the while loop short
        frequency = sorted(frequency, key=itemgetter(3))
        k = len(frequency) - 1

        # Create first cluster
        center_of_clusters = []
        add = [frequency[0][0], frequency[0][1], frequency[0][2], frequency[0][3], 1]
        center_of_clusters.append(add)

        # Find for all colour points a cluster
        while k >= 0:

            # Only colour points with enough presence
            if frequency[k][3] < 6:
                break
            else:
                belong1cluster = False

                # For every colour point calculate distance to all clusters
                for center in range(len(center_of_clusters)):
                    point_freq = np.array([frequency[k][0], frequency[k][1], frequency[k][2]])
                    point_center = np.array([center_of_clusters[center][0], center_of_clusters[center][1],
                                             center_of_clusters[center][2]])
                    distance = np.linalg.norm(point_freq - point_center)

                    # If a cluster is close enough, add this colour and recalculate the cluster
                    # Now the colour goes to the first cluster fullfilling this. Maybe it should be also the closest?
                    if distance <= 3:
                        new_count = center_of_clusters[center][3] + frequency[k][3]
                        new_center = [
                            int((
                                        point_freq[0] * frequency[k][3] + point_center[0] *
                                        center_of_clusters[center][
                                            3]) / new_count),
                            int((
                                        point_freq[1] * frequency[k][3] + point_center[1] *
                                        center_of_clusters[center][
                                            3]) / new_count),
                            int((
                                        point_freq[2] * frequency[k][3] + point_center[2] *
                                        center_of_clusters[center][
                                            3]) / new_count)]
                        center_of_clusters[center][0] = new_center[0]
                        center_of_clusters[center][1] = new_center[1]
                        center_of_clusters[center][2] = new_center[2]
                        center_of_clusters[center][3] = new_count
                        center_of_clusters[center][4] += 1
                        belong1cluster = True
                        break

                # Create new cluster if the colour point is not close enough to other clusters
                if belong1cluster == False:
                    add = [frequency[k][0], frequency[k][1], frequency[k][2], frequency[k][3], 1]
                    center_of_clusters.append(add)
                k -= 1

        # Only keep clusters with more than 5 colour entries
        new_center_of_clusters = []
        for x in range(len(center_of_clusters)):
            if center_of_clusters[x][4] > 5:
                new_center_of_clusters.append(center_of_clusters[x])

        # Number of clusters, not statistically relevant
        count_dynamic_cluster = len(new_center_of_clusters)

        # Average number of colours per cluster
        average_colour_dynamic_cluster = 0
        for x in range(len(new_center_of_clusters)):
            average_colour_dynamic_cluster += new_center_of_clusters[x][4]

        try:
            average_colour_dynamic_cluster = average_colour_dynamic_cluster / count_dynamic_cluster
        except ZeroDivisionError:
            average_colour_dynamic_cluster = 0

        result = [int(count_dynamic_cluster), int(average_colour_dynamic_cluster)]

        countColorDynamicDoc = ''
        avgColorDynamicDoc = ''

        print("#################HCI_Rule7_Dynamic_Clusters#################")
        print()

        # Detect Number of clusters, not statistically relevant
        print("Number of clusters, not statistically relevant: ")
        print(result[0])
        if 0 <= int(result[0]) <= 500:
            center_of_clusters = 'Less Colourful'
            countColorDynamicDoc = 'HCI_Rule7_Dynamic_Clusters'
            print("Less colourful")
        elif 501 <= int(result[0]) <= 1000:
            count_dynamic_cluster = 'Fair'
            print("Fair")
        elif 1001 <= int(result[0]):
            count_dynamic_cluster = 'Colourful'
            print("Colourful")

        print("Average number of colours per cluster: ")
        print(result[1])
        if 0 == int(result[1]):
            average_colour_dynamic_cluster = 'Meaningless'
            avgColorDynamicDoc = 'HCI_Rule7_Dynamic_Clusters'
            print("Meaningless")
        else:
            average_colour_dynamic_cluster = 'Average number of colours per cluster'
            print("Average number of colours per cluster")
            print("*********************************************")

        return [
            "Dynamic Cluster", "cp",
            ["Number of clusters, not statistically relevant", result[0], center_of_clusters, countColorDynamicDoc],
            ["Average number of colours per cluster", result[1], average_colour_dynamic_cluster, avgColorDynamicDoc]
        ]
