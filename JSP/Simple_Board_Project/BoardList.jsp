<%@ page contentType="text/html; charset=UTF-8" %>
<%@ page language="java" import="java.sql.*,java.util.*,java.text.*" %>

<HTML>
  <HEAD><TITLE>게시판</TITLE>
  </HEAD>
  <BODY>
    <P><P align=center><FONT color=#0000ff face=굴림 size=3><STRONG>자유 게시판
    </STRONG></FONT></P>
    <P>
      <CENTER>
        <TABLE border=0 width=600 cellpadding=4 cellspacing=0>
          <tr align="center">
            <td colspan="5" height="1" bgcolor="#1F4F8F"></td>
          </tr>
          <tr align="center" bgcolor="#87E8FF">
            <td width="42" bgcolor="#DFEDFF"><font size="2">번호</font></td>
            <td width="340" bgcolor="#DFEDFF"><font size="2">제목</font></td>
            <td width="84" bgcolor="#DFEDFF"><font size="2">등록자</font></td>
            <td width="78" bgcolor="#DFEDFF"><font size="2">날짜</font></td>
            <td width="49" bgcolor="#DFEDFF"><font size="2">조회</font></td>
          </tr>
          <tr align="center">
            <td colspan="5" bgcolor="#1F4F8F" height="1"></td>
          </tr>
<%
  Vector name=new Vector();
  Vector inputdate=new Vector();
  Vector email=new Vector();
  Vector subject=new Vector();
  Vector rcount=new Vector();

  int where=1;

  int totalgroup=0;
  int maxpages=2;
  int startpage=1;
  int endpage= startpage + maxpages - 1;
  int wheregroup=1;

  if (request.getParameter("go")!=null){
    where=Interger.parseInt(request.getParameter("go"));
    wheregroup=(where-1)/maxpages+1;
    where=startpage;
    endpage=startpage+maxpages-1;
  }
  int nextgroup=wheregroup+1;
  int priorgroup=wheregroup-1;

  int nextpage=where+1;
  int priorpage=where-1;
  int startrow=0;
  int endrow=0;

  int maxrows=2;
  int totalrows=0;
  int totalpages=0;

  int id=0;

  String em=null;
  Connection con=null;
  Statement st=null;
  ResultSet rs=null;

  try {
    Class.forName("org.git.mm.mysql.Driver");
  } catch (ClassNotFoundException e){
    out.println(e);
  }

  try {
    st=con.createStatement();
    rs=st.executeQuery("select * from freeboard order by id desc");

    if (!(rs.next())){
      out.println("게시판에 올린 글이 없습니다.");
    } else {
      do {
        name.addElement(rs.getString("name"));
        email.addElement(rs.getString("email"));
        String idate=rs.getString("inputdate");
        idate=idate.substring(0,8);
        inputdate.addElement(idate);
        subject.addElement(rs.getString("subject"));
        rcount.addElement(new Integer(rs.getInt("readcount")));
      } while(rs.next());
      totalrows=name.size();
      totalpages=(totalrows-1)/maxrows+1;
      startrow=(where-1)*maxrows;
    }
  }
