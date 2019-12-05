<%@ page contentType="text/html; charset=UTF-8" %>
<%@ page language="java" import="java.sql.*" %>
<%
Connection conn=null;
Statement st=null;
ResultSet rs=null;

try {
  Class.forName("com.mysql.jdbc.Driver");
} catch (ClassNotFoundException e) {
  out.println(e);
}

try {
  conn=DriverManager.getConnection("jdbc:mysql://localhost:3306/member?serverTimezone=UTC&useUnicode=true&charaterEncoding=euckr", "root", "root");
} catch (SQLException e) {
  out.println(e);
}

try {
  st=conn.createStatement();
  st.executeUpdate("create table woori(id char(10) primary key, name char(10))");
} catch (SQLException e) {
  out.println("e");
}

try {
  rs=st.executeQuery("select * from woori");
  ResultSetMetaData rsmd=rs.getMetaData();
  out.println("새로운 테이블이 생성되었습니다.<BR>");
  out.println(rsmd.getColumnCount()+"개의 컬럼(필드)을 가지고 있으며<BR>");
  out.println("첫 번째 컬럼은"+rsmd.getColumnName(1)+"<BR>");
  out.println("두 번째 칼럼은"+rsmd.getColumnName(2)+"<BR>");
  rs.close();
  st.close();
  conn.close();
} catch (SQLException e) {
  out.println(e);
}
%>
<a href=main.html>main으로</a>
