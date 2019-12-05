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
  st.executeUpdate("alter table woori modify name char(10) not null");
  st.executeUpdate("alter table woori add email char(30)");
  st.executeUpdate("alter table woori add password integer");
} catch (SQLException e) {
  out.println(e);
}

try {
  rs=st.executeQuery("select * from woori");
  ResultSetMetaData rsmd=rs.getMetaData();
  out.println("테이블이 수정 되었습니다.<br>");
  out.println(rsmd.getColumnCount()+"개의 컬럼(필드)을 가지고 있으며<br>");
  for (int i=1;i<=rsmd.getColumnCount();i++) {
    out.println(i+"번째 컬럼은"+rsmd.getColumnName(i));
    out.println("이고 유형은"+rsmd.getColumnTypeName(i));
    out.println("이며 크기는"+rsmd.getPrecision(i)+"<br>");
  }
  rs.close();
  st.close();
  conn.close();
} catch (SQLException e) {
  out.println(e);
}
%>
<a href=main.html>main으로</a>
