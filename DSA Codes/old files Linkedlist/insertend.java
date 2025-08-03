public class insertend{
    static class Node{
        int data;
        Node next;
        Node(int x){
            data = x;
            next = null;
        }
    }

    static Node insertatend(Node head, int x){
         Node temp = new Node(x);
         
         if(head == null) return temp;
         
         Node current = head;
         while(current.next!=null){
            current = current.next;
         }
         current.next = temp;
         return head;
    }


    public static void main(String[] args) {
       Node head = new Node(10);
       Node second = new Node(15);
       Node third = new Node(234);

        insertatend(head,5);

    }
}
