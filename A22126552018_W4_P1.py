import streamlit as lt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

name="Thrishank"
lt.title("This is our new program",anchor="Apress")
lt.text("Hello")
lt.text("Hello World")
lt.header("This is our header")
lt.subheader("This is our sub header")
lt.caption("This is caption")
lt.text(name)

lt.markdown("# Hi,\n# ***People*** \t!!!!!!!!!")
lt.markdown('## Welcome to')
lt.markdown("""### Streamlit's World""")

lt.subheader("""Python Code""")
code = '''def hello():
 print("Hello, Streamlit!")'''
lt.code(code, language='python')

lt.write(input)


lt.subheader("""Java Code""")
lt.code("""public class GFG {
 public static void main(String args[])
 {
 System.out.println("Hello World");
 }
}""", language='java')
lt.subheader("""JavaScript Code""")
lt.code(""" <p id="demo"></p>
<script>
try {
 adddlert("Welcome guest!");
}
catch(err) {
 document.getElementById("demo").innerHTML = err.message;
}
</script> """)


df = pd.DataFrame(
 np.random.randn(30, 10),
 columns=('col_no %d' % i for i in range(10)))
lt.dataframe(df.style.highlight_min(axis=1))

lt.table(df)

lt.metric(label="Temperature", value="31 °C", delta="1.2 °C")

c1, c2, c3 = lt.columns(3)
# Defining Metrics
c1.metric("Rainfall", "100 cm", "10 cm")
c2.metric(label="Population", value="123 Billions", delta="1 Billions", delta_color="inverse")
c3.metric(label="Customers", value=100, delta=10, delta_color="off")
lt.metric(label="Speed", value=None, delta=0)
lt.metric("Trees", "91456", "-1132649")


lt.json
(
 { "Books" : 
 [{
 "BookName" : "Python Testing with Selenium",
 "BookID" : "1",
 "Publisher" : "Apress",
 "Year" : "2021",
 "Edition" : "First",
 "Language" : "Python",
 },
 {
 "BookName": "Beginners Guide to Streamlit with Python",
 "BookID" : "2",
 "Publisher" : "Apress",
 "Year" : "2022",
 "Edition" : "First",
 "Language" : "Python"
 }]
 }
)

