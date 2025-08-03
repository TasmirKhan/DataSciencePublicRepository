public class insertbegin{
    static class Node{
        int data;
        Node next;
        Node(int x){
            data = x;
            next = null;
        }
    }

    static Node insertatbegining(Node head, int x){
         Node temp = new Node(x);
         temp.next = head;
         return temp;
    }


    public static void main(String[] args) {
       Node head = new Node(10);
       Node second = new Node(15);
       Node third = new Node(234);

        insertatbegining(head,5);

    }
}
