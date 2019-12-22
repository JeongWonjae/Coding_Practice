import com.mysql.cj.xdevapi.Statement;
import java.sql.*;

public class MysqlConnect {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
			
		java.sql.Connection conn=null;
		java.sql.Statement stmt=null;
		java.sql.ResultSet rs=null;

		try {
			conn=DriverManager.getConnection("jdbc:mysql://localhost:3306/mqttdb?serverTimezone=UTC&useUnicode=true&charaterEncoding=euckr", "root", "root");
			System.out.println("success connect!");
		} catch(Exception e) {
			System.out.println("error~!" +e);
		}
		
		try {
			
			stmt = conn.createStatement();
			rs = stmt.executeQuery("select * from sub_db;");
			
			while(rs.next()){
                //Ãâ·Â
                System.out.println(rs.getString("token"));
                System.out.println(rs.getString("seed"));
 
            }
 
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			if(conn!=null) {
				try {
					conn.close();
				} catch (Exception e) {}
			}
		}  
		
	}
}
