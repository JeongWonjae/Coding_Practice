<%@ page contentType="text/html; charset=UTF-8" %>
<%@ page language="java" import="java.sql.*" %>
<% request.setCharacterEncoding("euc-kr"); %>
<%
String id=request.getParameter("id");
int password=Integer.parseInt(request.getParameter("password"));
String name=request.getParameter("name");
String email=request.getParameter("email");
String sql=null;
Connection conn=null;
Statement st=null;
ResultSet rs=null;
int cnt=0;

try {
  Class.forName("com.mysql.jdbc.Driver");
} catch (ClassNotFoundException e) {
  out.println(e.getMessage());
}

try {
  conn=DriverManager.getConnection("jdbc:mysql://localhost:3306/member?serverTimezone=UTC&useUnicode=true&charaterEncoding=euckr","root","root");
  st=conn.createStatement();
  rs=st.executeQuery("select * from woori where id='"+id+"'");
  if (!(rs.next())){
    sql="insert into woori(id,password,name,email)";
    sql=sql+"values('"+id+"',"+password+",";
    sql=sql+"'"+name+"','"+email+"')";
    cnt=st.executeUpdate(sql);
    if(cnt>0)
      out.println("데이터가 성공적으로 입력되었습니다.");
    else
      out.println("데이터가 입력되지 않았습니다.");
  } else
    out.println("id가 이미 등록되어 있었습니다.");
  st.close();
  conn.close();
} catch (SQLException e){
  out.println(e.getMessage());
}
%>
<a href="main.html">main으로</a>
&nbsp;<a href="insert.html">회원등록페이지로</a>
