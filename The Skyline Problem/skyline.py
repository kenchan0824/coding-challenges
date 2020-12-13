from bisect import insort

def eventscan(buildings):

    events = []
    for l, r, h in buildings:
        events.append([l, -h])                      # ensure incomming event goes first
        events.append([r, h])                       # outgoing event
    events = sorted(events)                         # order events by time
    
    heights = []                                    # stacked heights
    skyline = []                                    # results
    max_height = 0                                  # handle corner cases
    
    for t, h in events:

        if h < 0:                                   # incomming event
            insort(heights, h)                      # negative value, ensure max first
            if -h > max_height:
                skyline.append([t, -h])
                max_height = -h
        else:                                       # outgoing event
            heights.remove(-h)
            curr_height = -heights[0] if heights else 0
            if curr_height < max_height:            # handle corner cases
                max_height = curr_height
                skyline.append([t, max_height])

    return skyline


if __name__ == '__main__':
    
    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    eventscan(buildings)
#    skyline = [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

    buildings = [[0,2,3],[2,5,3]]  # corner case
    eventscan(buildings)
#    skyline = [[0,3], [5,0]]    
    
