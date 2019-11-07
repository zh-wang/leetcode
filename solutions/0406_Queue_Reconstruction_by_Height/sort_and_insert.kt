import java.util.*
class Solution {
    fun reconstructQueue(people: Array<IntArray>): Array<IntArray> {
        // sort people with desceding height and ascending k
        val sortedPeople = people.sortedWith(
            Comparator { x, y -> if (x[0] == y[0]) y[1] - x[1] else x[0] - y[0] }
        )
        var ret = Array<IntArray>(people.size) { intArrayOf() }
        // go through from the lowest people,
        // we move a point from head of ret `k` times, if its pointed slot is empty
        // when it stops, put the people into that slot
        for (pair in sortedPeople) {
            var steps = pair[1]
            for (i in 0..ret.size-1) {
                if (ret[i].isNotEmpty()) continue // skip all non-empty slot
                if (steps == 0) { // when no steps remains, fill the slot
                    ret[i] = pair
                }
                --steps // reduce steps each time encounting an empty slot
            }
        }
        return ret
    }
}
