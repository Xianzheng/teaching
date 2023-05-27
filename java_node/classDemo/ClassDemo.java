package classDemo;
// import java.util.Scanner;
public class ClassDemo {
    
    public static void main(String []args){
        // display something show your main logic
        // Scanner scan = new Scanner(System.in);
        MakeStudent makeStudent = new MakeStudent();

        Student stu = makeStudent.make("Mark", "asd");
        System.out.println(stu.getName());
        System.out.println(stu.getId());
        
    }
}

class MakeStudent {

    public Student make(String name, String id){
        Student stu = new Student();
        stu.setName(name);
        stu.setId(id);
        return stu;
    }
}



