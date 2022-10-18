'''n=int(input())
c=0
a=list(map(int,input().split()))
flag=True
while (True):
    flag = True
    i = 1
    while (i < len(a) - 1):
        for i in a:
            if a[i]<a[i+1]:
                del a[i+1]
                flag=False
            if flag:
                break
            else:
                c+=1
    print(c)'''
'''
import java.util.ArrayList;
import java.util.Scanner;
public class StudentViva {
 public static void main(String[] args) {
 Scanner sc = new Scanner(System.in);
 int n = sc.nextInt();
 ArrayList<Integer> al = new ArrayList<>();
 for(int i=0; i<n; i++) {
 al.add(sc.nextInt());
 }
 int c = 0;
 while(true) {
 boolean flag = true;
 for(int i=1; i<al.size()-1; i++) {
 if(al.get(i) > al.get(i-1) ) {
 al.remove(i);
 flag = false;
 }
 }
 if(flag) {
 break;
 }else {
 c++;
 }
 }
 System.out.println(c);
 }
}
'''

class StudentViva:
    @staticmethod
    def main(args):
        sc = "Python-inputs"
        n = input()
        al = []
        i = 0
        while (i < n):
            al.append(input())
            i += 1
        c = 0
        while (True):
            flag = True
            i = 1
            while (i < len(al) - 1):
                if (al[i] > al[i - 1]):
                    del al[i]
                    flag = False
                i += 1
            if (flag):
                break
            else:
                c += 1
        print(c)


if __name__ == "__main__":
    StudentViva.main([])
