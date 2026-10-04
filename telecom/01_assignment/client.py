import json 
import sys

def linkKey(a, b):
    return tuple(sorted([a, b]))

def getLinksInCircuit(circuit):
    links = []
    for i in range(len(circuit) - 1):
        links.append(linkKey(circuit[i], circuit[i + 1]))
    return links 

def canAllocate(circuit, demand, capacity):
    for link in getLinksInCircuit(circuit):
        if capacity[link] < demand:
            return False
    return True

def allocate(circuit, demand, capacity):
    for link in getLinksInCircuit(circuit):
        capacity[link] -= demand

def deallocate(circuit, demand, capacity):
    for link in getLinksInCircuit(circuit):
        capacity[link] += demand

def main():
    with open(sys.argv[1], 'r') as f:
        data = json.load(f)
    
    possibleCircuits = data['possible-circuits']
    duration = data['simulation']['duration']
    demands = data['simulation']['demands']

    # build dictionary: {(A, S1): 10.0, (S1, S3): 10.0, ...}
    capacity = {}
    for link in data['links']:
        key = linkKey(link['points'][0], link['points'][1])
        capacity[key] = link['capacity']

    allocatedPaths = {}
    eventNum = 0

    for t in range(1, duration + 1):
        for idx, demand in enumerate(demands):
            if demand['end-time'] == t and idx in allocatedPaths:
                circuit = allocatedPaths[idx]
                deallocate(circuit, demand['demand'], capacity)
                del allocatedPaths[idx]
                ep = demand['end-points']
                eventNum += 1
                print(f"{eventNum}. demand deallocation: {ep[0]}<->{ep[1]} st:{t}")

        for idx, demand in enumerate(demands):
            if demand['start-time'] == t:
                ep = demand['end-points']
                eventNum += 1
                success = False

                for circuit in possibleCircuits:
                    matchesForward = circuit[0] == ep[0] and circuit[-1] == ep[1]
                    matchesReverse = circuit[0] == ep[1] and circuit[-1] == ep[0]

                    if matchesForward or matchesReverse:
                        if canAllocate(circuit, demand['demand'], capacity):
                            allocate(circuit, demand['demand'], capacity)
                            allocatedPaths[idx] = circuit
                            success = True
                            break
                
                if success:
                    print(f"{eventNum}. demand allocation: {ep[0]}<->{ep[1]} st:{t} - successful")
                else:
                    print(f"{eventNum}. demand allocation: {ep[0]}<->{ep[1]} st:{t} - unsuccessful")

if __name__ == "__main__":
    main()
    
