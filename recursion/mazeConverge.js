function largestCycle(edges) {
    var result, visitedFrom, startCell, cell, cells;
    
    result = [];
    visitedFrom = Array(edges.length).fill(-1);
    for (startCell = 0; startCell < edges.length; startCell++) {
        cells = [];
        for (cell=startCell; cell>-1 && visitedFrom[cell]===-1; cell = edges[cell]) {
            visitedFrom[cell] = startCell;
            cells.push(cell);
        }
        if (cell > -1 && visitedFrom[cell] === startCell) {
            cells = cells.slice(cells.indexOf(cell));
            if (cells.length > result.length) result = cells;
        }
    }
    return result;
}

// Snippet I/O

var input = '4 4 1 4 13 8 8 8 0 8 14 9 15 11 -1 10 15 22 22 22 22 22 21';
var output = '';

(input.oninput = function () {
    // Get input as array of numbers
    var edges = input.trim().split(/\s+/).map(Number);
    // Apply algorithm
    var cycle = largestCycle(edges);
    console.log(cycle);
    // Output result
    // output.textContent = cycle.length + ': ' + JSON.stringify(cycle);
})(); // Execute also at page load

// Input:<br>
// <textarea style="width:100%">4 4 1 4 13 8 8 8 0 8 14 9 15 11 -1 10 15 22 22 22 22 22 21</textarea></br>
// Greatest : <span></span>