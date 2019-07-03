class Solution {
    func setZeroes(_ matrix: inout [[Int]]) {
        let m = matrix.count
        let n = matrix[0].count
        for i in 0..<m {
            for j in 0..<n {
                if (matrix[i][j] != 0) {
                    continue
                }
                for p in 0..<m {
                    if (matrix[p][j] > Int.min && matrix[p][j] != 0) {
                         matrix[p][j] = Int.min
                    }
                }
                for q in 0..<n {
                    if (matrix[i][q] > Int.min && matrix[i][q] != 0) {
                        matrix[i][q] = Int.min
                    }
                }
            }
        }
        for i in 0..<m {
            for j in 0..<n {
                if (matrix[i][j] == Int.min) {
                    matrix[i][j] = 0
                }
            }
        }
    }
}
