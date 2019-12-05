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
%> <%
try {
  st=conn.createStatement();
  rs=st.executeQuery("select * from woori order by id"); %>
<html>
<body>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<h3>회원 정보 보기</h3>
<table border=1>
  <tr>
    <th>사용자 ID</th>
    <th>이름</th>
    <th>이메일</th>
  </tr>
  <%
  if(!(rs.next())) { %>
    <tr><td clospan=4>등록된 회원이 없습니다.</td></tr>
  <% } else {
    do {
      out.println("<tr>");
      out.println("<td>"+rs.getString("id")+"</td>");
      out.println("<td>"+rs.getString("name")+"</td>");
      out.println("<td>"+rs.getString("email")+"</td>");
      out.println("</tr>");
    } while (rs.next());
  }
  rs.close();
  st.close();
  conn.close();
} catch (SQLException e){
  System.out.println(e);
}
%>
</table>
  <a href="main.html">main으로</a>
  &nbsp
  <a href="insert.html">회원 등록 페이지로</a>
</body>
</html>
