+a=[]
+b=[]
+c=[]
+n=int(input("Enter length of Array"))
+
+print("Enter array : ")
+
+for i in range(n):
+    x=int(input())
+    a.insert(i,x)
+
+
+for i in range(n):
+    for j in range(n):
+        if i!=j:
+            b.insert(j,a[i]*a[j])
+        j=j+1
+    l=b[0]
+    for k in range(n-1):
+        if l<b[k]:
+            l=b[k]
+        k=k+1
+    c.insert(i,l)
+    i=i+1
+
+for k in range(n-1):
+        if l<c[k]:
+            l=c[k]
+        k=k+1
+for i in range(n):
+    for j in range(i,n):
+        if l==a[i]*a[j]:
+         print("Pair = ( ",a[i]," , ",a[j],")")   
+        j=j+1
+    i=i+1