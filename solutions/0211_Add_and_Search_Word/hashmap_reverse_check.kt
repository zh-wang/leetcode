class WordDictionary() {

    /** Initialize your data structure here. */
    var checker = hashSetOf<String>()

    /** Adds a word into the data structure. */
    fun addWord(word: String) {
        checker.add(word)
    }

    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    fun search(word: String): Boolean {
        for (w in checker) {
            if (word.length != w.length) continue
            var ret = true
            for (i in 0..word.length-1) {
                if (word[i] != w[i] && word[i] != '.') {
                    ret = false
                    continue
                }
            }
            if (ret) return true
        }
        return false
    }

}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
