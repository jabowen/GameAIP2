def find_path (source_point, destination_point, mesh):        """    Searches for a path from source_point to destination_point through the mesh            Args:        source_point: starting point of the pathfinder                        destination_point: the ultimate goal the pathfinder must reach        mesh: pathwayconstraints the path adheres to    Returns:                A path (list of points) from source_point to destination_point if exists           A list of boxes explored by the algorithm    """        path = []        boxes = {}    point_boxes = []        # search for source box    source_x = source_point[0]    source_y = source_point[1]    for box in mesh['boxes']:        coords = box # each box is a list of 4 points forming rectangle (x1,x2,y1,y2)        box_x1 = coords[0]        box_x2 = coords[1]        box_y1 = coords[2]        box_y2 = coords[3]                # check to see if point (source) exists within the box        if (source_x > box_x1 and source_x < box_x2 and source_y > box_y1 and source_y < box_y2):            # point remains within the box, source box becomes this box point_boxes[0]            point_boxes.append(box)            break        # search for destination box    destination_x = destination_point[0]    destination_y = destination_point[1]    for box in mesh['boxes']:        coords = box # each box is a list of 4 points forming rectangle (x1,x2,y1,y2)        box_x1 = coords[0]        box_x2 = coords[1]        box_y1 = coords[2]        box_y2 = coords[3]                # check to see if point (source) exists within the box        if (destination_x > box_x1 and destination_x < box_x2 and destination_y > box_y1 and destination_y < box_y2):            # point remains within the box, destination box becomes this box point_boxes[1]            point_boxes.append(box)            break        # check if both boxes exist    if(len(point_boxes)<2):       print('the source or destination is unreachable')       return path, boxes.keys()    if (point_boxes[0] == None):       print('Source box does not exist!')       return path, boxes.keys()     if (point_boxes[1] == None):        print ('Destination box does not exist!')        return path, boxes.keys()        #djiksta's    queue = [(point_boxes[0],Euclidean_distance(point_boxes[0], point_boxes[1]),0)]    queue.append((point_boxes[1], Euclidean_distance(point_boxes[0], point_boxes[1]),1))    boxes[point_boxes[0]] = 0    boxes[point_boxes[1]] = 0    Previous={point_boxes[0]: None, point_boxes[1]: None}    ids = {point_boxes[0]: 0, point_boxes[1]: 1}    notFound = True    if (point_boxes[0]==point_boxes[1]):        boxes[point_boxes[1]] = Euclidean_distance(point_boxes[0], point_boxes[1])        path.append(source_point)        path.append(destination_point)        return path, boxes.keys()    while(len(queue)>0 and notFound):        current = queue[0][0]        currentDist = queue[0][1]        currentID = queue[0][2]        queue.remove((current,currentDist,currentID))        neighbors=(mesh['adj'].get(current))        for neighbor in neighbors:            pastCost = Euclidean_distance(neighbor, current)+boxes[current]            if(currentID == 0):                dist = Euclidean_distance(neighbor, point_boxes[1])            else:                dist = Euclidean_distance(neighbor, point_boxes[0])                            if not(neighbor in boxes):               queue.append((neighbor,dist,currentID))               boxes[neighbor] = pastCost               Previous[neighbor] = current               ids[neighbor] = currentID                           elif (ids[neighbor]!=currentID):                notFound = False                if(currentID==1):                    endpoints = [neighbor,current]                else:                    endpoints = [current,neighbor]                break                           elif (boxes[neighbor] > pastCost):                boxes[neighbor] = pastCost                Previous[neighbor] = current        queue.sort(key=byDist)            if(notFound):        print("no path possible")        return path, boxes.keys()             current = endpoints[0]    while(Previous[current]!=None):        path.append(((current[0]+current[1])/2,(current[2]+current[3])/2))        current = Previous[current]    path.append(source_point)        path.reverse()        current = endpoints[1]    while(Previous[current]!=None):        path.append(((current[0]+current[1])/2,(current[2]+current[3])/2))        current = Previous[current]    path.append(destination_point)    return path, boxes.keys()    def byDist(e):    return e[1]def Euclidean_distance(sourcePoint, destinationPoint):    sourceX = sourcePoint[0]    sourceY = sourcePoint[1]    destinationX = destinationPoint[0]    destinationY = destinationPoint[1]    distance = pow((pow((destinationX-sourceX), 2) + pow((destinationY-sourceY), 2)),.5)    return distance