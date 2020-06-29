import mathdef find_path (source_point, destination_point, mesh):
    """    Searches for a path from source_point to destination_point through the mesh    Args:        source_point: starting point of the pathfinder        destination_point: the ultimate goal the pathfinder must reach        mesh: pathway constraints the path adheres to
    Returns:
        A path (list of points) from source_point to destination_point_point if exists        A list of boxes explored by the algorithm    """        # discover source_point and destination_point     point_boxes = []        # search for source box    source_x = source_point[0]    source_y = source_point[1]    for boxes in mesh.boxes:        coords = boxes # each box is a list of 4 points forming rectangle (x1,x2,y1,y2)        box_x1 = coords[0]        box_x2 = coords[1]        box_y1 = coords[2]        box_y2 = coords[3]                # check to see if point (source) exists within the box        if (source_x > box_x1 and source_x < box_x2 and source_y > box_y1 and source_y < box_y2):            # point remains within the box, source box becomes this box point_boxes[0]            point_boxes[0] = boxes            break        # search for destination box    destination_x = destination_point[0]    destination_y = destination_point[1]    for boxes in mesh.boxes:        coords = boxes # each box is a list of 4 points forming rectangle (x1,x2,y1,y2)        box_x1 = coords[0]        box_x2 = coords[1]        box_y1 = coords[2]        box_y2 = coords[3]                # check to see if point (source) exists within the box        if (destination_x > box_x1 and destination_x < box_x2 and destination_y > box_y1 and destination_y < box_y2):            # point remains within the box, destination box becomes this box point_boxes[1]            point_boxes[1] = boxes            break        # check if both boxes exist    if (point_boxes[0] == None):       print('Source box does not exist!')    if (point_boxes[1] == None):        print ('Destination box does not exist!')        # finished checking source and destination boxes - run BFS (Breadth-First Search)    # point_boxes[0] should be the source box and point_boxes[1] should be the destination box    BFS_result = modified_BFS(mesh, point_boxes[0], point_boxes[1])        # check to see if a valid path exists - check if destination box is in BFS_result    if (point_boxes[1] not in BFS_result):        print ('No path!')        return        # Dijkstra's start    queue = []        heappush(queue, (source_point, 0))        came_from = {}    cost_so_far = {}        came_from[source_point] = None    cost_so_far[source_point] = 0        while queue:        current_cell, current_cost = heappop(queue)        if current_cell == destination_point:            current = destination_point            path = []            while current != source_point:                path.append(current)                current = came_from[current]            path.append(source_point)            path.reverse()            return path        for adjacent_cell, adjacent_cell_cost in adj(mesh, current_cell):            new_path_cost = current_cost + adjacent_cell_cost             if adjacent_cell not in cost_so_far or new_path_cost < cost_so_far[adjacent_cell]:                cost_so_far[adjacent_cell] = new_path_cost                heappush(queue, (adjacent_cell, new_path_cost))                came_from[adjacent_cell] = current_cell        # Dijkstra's end    path = []    boxes = {}    return path, boxes.keys()# modified BFS - determines if path from source to destination exists# and keeps track of precision points - held in global detail_points for# generating a legal line segment to goaldef modified_BFS(mesh, sourceBox, destinationBox):    # dict to keep precise position - global so it may be accessed outside of BFS    detail_points = {}    detail_points[0] = (sourceBox[0], sourceBox[1])        visited = []    queue = [sourceBox]        counter = 1    while queue:        box = queue.pop(0)        if box not in visited:            visited.append(box)            neighbors = mesh.get(box)                        # --- modified part ---            # creates a line segment increaming from 0 to the amount of lines needed to get to the destination            # a dictionary with [lineNumber, (x,y) pair], tries to fetch least distance corner vertex when moving            if (box == sourceBox): # if source, move along edges for                x = sourceBox[0]                y = sourceBox[1]                nextBox = neighbors[0]                 check_box_x1 = coords[0]                check_box_x2 = coords[1]                check_box_y1 = coords[2]                check_box_y2 = coords[3]                if (nextBox != None):                    if (check_box_x1 - x < check_box_x2 - x): # x1 is closer                        x_to_go = check_box_x1                    else: # x2 is closer                        x_to_go = check_box_x2                    if (check_box_y1 - y < check_box_y2 - y): # y1 is closer                        y_to_go = check_box_y1                    else: # y2 is closer                        y_to_go = check_box_y2                                # add to detail_points                detail_points[counter] = x_to_go, y_to_go                counter += 1                                else:                # find nearest vertex point of box from previous point                coords = box                box_x1 = coords[0]                box_x2 = coords[1]                box_y1 = coords[2]                box_y2 = coords[3]                                # check nearest box                nextBox = neighbors[0]                                 if (nextBox != None):                    if (check_box_x1 - x < check_box_x2 - x): # x1 is closer                        x_to_go = check_box_x1                    else: # x2 is closer                        x_to_go = check_box_x2                    if (check_box_y1 - y < check_box_y2 - y): # y1 is closer                        y_to_go = check_box_y1                    else: # y2 is closer                        y_to_go = check_box_y2                        detail_points[counter] = x_to_go, y_to_go            counter += 1            # --- modified part ---                        for neighbor in neighbors:                queue.append(neighbor)                    return visited    def Euclidean_distance(sourcePoint, destinationPoint):    sourceX = sourcePoint[0]    sourceY = sourcePoint[1]    destinationX = destinationPoint[0]    destinationY = destinationPoint[1]    distance = math.sqrt(pow((destinationX-sourceX), 2) + pow((destinationY-sourceY), 2))    return distance