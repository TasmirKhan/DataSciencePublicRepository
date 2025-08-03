package DSA Codes.Linkedlist;

public class Bnd{
    class Node{
        int data;
        Node next;
    }

    void recursivetraversal(Node head){
        
        if(head==null){
            return;
        }
        System.out.println(head.data);
        recursivetraversal(head.next);
    }

    void Traversing(Node head){
        Node curr = head; int a=0;
        while(curr!=null){
            // System.out.print(curr.data+"->");
            a = a+1;
            curr = curr.next;
        }
    }

    public static void main(String[] args){
        Bnd obj = new Bnd();
            Bnd.Node head = obj.new Node();
            Bnd.Node second = obj.new Node();
            Bnd.Node third = obj.new Node();
            head.data=10; head.next=second;
            second.data =20;second.next = third;
            third.data =30; third.next = null;
           
            obj.Traversing(head);
            // It's Alternative method is make the node static

    }
}
