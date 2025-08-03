class Node{
    int data;
    Node next;
    Node(int x){
        data = x;
        next = null;
    }
}

class Ast{
    public static void printlist(Node head){
        Node curr = head;
        while(curr!=null){
            System.out.println(curr.data+"->");
            curr = curr.next;
        }
        return ;
    }
    public static void main(String[] args) {
    Node head = new Node(10);
    Node Second = new Node(20);
    Node third = new Node(30);
    head.next=Second;
    Second.next = third;
    System.out.println("Linked list = ");
    printlist(head);

}

}