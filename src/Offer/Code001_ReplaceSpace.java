package Offer;

public class Code001_ReplaceSpace {
    public static void main(String[] args) {
        StringBuffer str = new StringBuffer("we are here");
        String result = replaceSpace2(str);
        System.out.println(result);
    }

    //running time 18ms,occupied memory 9675k
    public static String replaceSpace0(StringBuffer str) {
        return str.toString().replaceAll("\\s", "%20");
    }


    public static String replaceSpace2(StringBuffer str) {
        int spaceNum = 0;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == ' ') {
                spaceNum++;
            }
        }
        int oldIndex = str.length() - 1;
        str.setLength(str.length() + spaceNum * 2);
        int newIndex = str.length() - 1;
        for (; newIndex > 0 & oldIndex > 0; newIndex--) {
            if (str.charAt(oldIndex) == ' ') {
                str.setCharAt(newIndex--, '0');
                str.setCharAt(newIndex--, '2');
                str.setCharAt(newIndex, '%');
            } else {
                str.setCharAt(newIndex, str.charAt(oldIndex));
            }
            oldIndex--;
        }
        return str.toString();
    }

    public static String replaceSpace3(StringBuffer str) {
        if (str == null)
            return null;
        StringBuffer result = new StringBuffer();
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == ' ') {
                result.append('%');
                result.append('2');
                result.append('0');
            } else
                result.append(str.charAt(i));
        }
        return result.toString();
    }
}
