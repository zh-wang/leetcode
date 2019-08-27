class LRUCache {

    class Node {
        int key;
        int value;
        Node prev = null;
        Node next = null;
        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    Node head, tail;
    int count;
    int limit;
    Map<Integer, Node> map;

    public LRUCache(int capacity) {
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head.next = tail;
        tail.prev = head;
        count = 0;
        map = new HashMap<>();
        limit = capacity;
    }

    public int get(int key) {
        if (map.containsKey(key)) {
            Node cur = map.get(key);
            remove(cur);
            insert(cur, head);
            return cur.value;
        } else {
            return -1;
        }
    }

    public void put(int key, int value) {
        if (map.containsKey(key)) {
            Node cur = map.get(key);
            cur.value = value;
            remove(cur);
            insert(cur, head);
        } else {
            if (count == limit) {
                Node last = tail.prev;
                map.remove(last.key);
                remove(last);
                count -= 1;
            }
            Node newNode = new Node(key, value);
            map.put(key, newNode);
            insert(newNode, head);
            count += 1;
        }
    }

    private void insert(Node target, Node l) {
        // no null check
        Node r = l.next;
        target.prev = l;
        target.next = r;
        l.next = target;
        r.prev = target;
    }

    private void remove(Node target) {
        // no null check
        target.prev.next = target.next;
        target.next.prev = target.prev;
        target.prev = null;
        target.next = null;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
