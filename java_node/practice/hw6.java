package practice;
public class hw6 {
    public static void main (String []args){
        book fire= new book();
        fire.setbookName("world of fire");
        fire.setbookNum("32");
        fire.setRating("4 stars");
        fire.setGenre("Fantasy");
        fire.setPages("348");
        book alone=new book();
        alone.setbookName("Alone in a lonely night");
        alone.setbookNum("03");
        alone.setRating("2 stars");
        alone.setGenre("Suspense,Drama");
        alone.setPages("225");
        book highschool= new book();
        highschool.setbookName("Life of a student");
        highschool.setbookNum("494");
        highschool.setRating("5 stars");
        highschool.setGenre("Drama,Action");
        highschool.setPages("500");
        book space= new book();
    
        space.setbookName("Guide to survive in space");
        space.setbookNum("486");
        space.setRating("4 stars");
        space.setGenre("Bibliography");
        space.setPages("600");
        book kingdom= new book();
        kingdom.setbookName("Magical kingdom");
        kingdom.setbookNum("02");
        kingdom.setRating("2 stars");
        kingdom.setGenre("Fantasy");
        kingdom.setPages("836");

        Library lib = new Library();

        lib.putBook(fire);
        lib.putBook(alone);
        lib.putBook(highschool);
        lib.putBook(space);
        lib.putBook(kingdom);

        book findone = lib.findBookName("world of fire");
        if (findone != null){
            System.out.println(findone.getRating());
        }{
            System.out.println("this book does not exist");
        }
        // remove book world of fire
        lib.removeBook(0);
        System.out.println("we remove book world of fire");

        book findone1 = lib.findBookName("world of fire");
        if (findone1 != null){
            System.out.println(findone1.getRating());
        }{
            System.out.println("this book does not exist");
        }
        // book bookbyFind = lib.findBookName("fire");
        // System.out.println(bookbyFind.getbookName());
        // book[] array= new book[5];

        
        // array[0]=fire;
        // array[1]=alone;
        // array[2]=highschool;
        // array[3]=space;
        // array[4]=kingdom;

        
    }
}

//standstard
class book{
    
    private String bookName="";
    private String bookNum="";
    private String bookRating="";
    private String bookGenre="";
    private String bookPages="";

    public void setbookName(String name){
        this.bookName=name;
    }
    public void setbookNum(String num){
        this.bookNum=num;
        }
    public void setRating(String num){
        this.bookRating=num;
    }
    public void setGenre(String name){
        this.bookGenre=name;
        }
    public void setPages(String num){
       this.bookPages=num;
        }
        public String getbookName(){
            return this.bookName;
        }
        public String getbookNum(){
            return this.bookNum;
            }
        public String getRating(){
            return this.bookRating;
        }
        public String getGenre(){
            return this.bookGenre;
            }
        public String getPages(String num){
            return this.bookPages;
            }
}

class Library{
    //make a store; store is a  Array, it only has 5 position to put book

     book[] store = new book[5];

    //it has a library method called putBook, it can put books into store


    public void putBook(book b){
        for(int i = 0; i<5;i++){
            // System.out.println(store[i]);
            
            if( store[i] == null){
                store[i] = b;
                break;
            }
        }
    }

    //it has a library method called findBookByName using books name to find, it can search book to find, return book 
    public book findBookName(String b){
        String found="";
        book findone = null;
        for (int i = 0; i < store.length; i++){
            if (this.store[i] != null){
                if (this.store[i].getbookName() == b){
                    findone =  this.store[i];
                }
            }
        }
        // for(book i: store){
            
        //     if (i.getbookName()==b){
        //         found=b;
        //         return i;
        //     }
        // }
       
        return findone;
    }

    //it has a library method called findBookByRate using books rating to find, return an Array
    // 4 starts, [book1, book4]

    //create a new method removeBook(int pos)
    public void removeBook(int pos){
        this.store[pos] = null;
        
    }

    //create a new method replaceBook(int pos, book b)
}


//homework:
