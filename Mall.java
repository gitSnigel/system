import java.util.Hashtable;

public class Fail {

    public static String decodeCode(String encodedString) {
        String  decodedString = "";
        Hashtable h = new Hashtable();
        h.put('2',new Character('a'));
        h.put('3',new Character('d'));
        h.put('4',new Character('g'));
        h.put('5',new Character('j'));
        h.put('6',new Character('m'));
        h.put('7',new Character('p'));
        h.put('8',new Character('t'));
        h.put('9',new Character('w'));
        h.put('0',new Character(' '));

        int i=0,j;
        while(i < encodedString.length()) {
            if( !Character.isDigit(encodedString.charAt(i)) ) {
                return null;
            }

            if(encodedString.charAt(i) == '#') {
                i++;
                continue;
            }
            j=i;
            while(i<(encodedString.length()-1) && (encodedString.charAt(i+1) == encodedString.charAt(i)) )
                i++;

            decodedString = decodedString + (char)(  ((Character)h.get(encodedString.charAt(j))).charValue() + (i-j)  );
            i++;
        }

        return  decodedString;
    }

    public static void main(String[] args) {

    }
}