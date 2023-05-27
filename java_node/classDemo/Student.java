package classDemo;
// inner class
public class Student{

    private String studentName = "";
    private String studentId = "";

    public void setName(String name){
        this.studentName = name;
    }

    public void setId(String id){
        this.studentId = id;
    }

    public String getName(){
        return this.studentName;
    }

    public String getId(){
        return this.studentId;
    }

}
