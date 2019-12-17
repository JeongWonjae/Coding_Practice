import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

public class JsonLib {

	public static void main(String[] args) throws ParseException {
		// TODO Auto-generated method stub

		//PASING GSON DATA
		//brace = {} = object , square brackets = [] = array
		String str="[{'NO':1, 'NAME':'WONJAE', 'AGE':25},"
				+ "{'NO':2, 'NAME':'JAVA', 'AGE':'IDONKNOW'}]";
		JsonParser jsonParser=new JsonParser();
		JsonArray jsonArray=(JsonArray) jsonParser.parse(str);
		
		for(int i=0; i<jsonArray.size();i++) {
			JsonObject object=(JsonObject) jsonArray.get(i);
			String NO=object.get("NO").getAsString();
			String NAME=object.get("NAME").getAsString();
			String AGE=object.get("AGE").getAsString();

			System.out.println(NO);
			System.out.println(NAME);
			System.out.println(AGE);
			System.out.println();

		}
		//exist key
		//대괄호를 구분하는 키가 있기 때문에 parser를 먼저 object로 파싱함.
		str="{'GAME':[{'NO':1, 'NAME':'SUDDENATTACK', 'GENRE':'FPS'},"
				+ "{'NO':2, 'NAME':'MAPLESTORY', 'GENRE':'RPG'}],"
				+ "'COMPUTER':[{'NO':1, 'NAME':'LAPTOP'},"
				+ "{'NO':2, 'NAME':'DESKTOP'}]}";
		JsonParser jsonParser2=new JsonParser();
		JsonObject jsonObj=(JsonObject) jsonParser2.parse(str);
		
		JsonArray jsonArray2=(JsonArray) jsonObj.get("GAME");
		System.out.println("***GAME***");
		for(int i=0;i<jsonArray2.size();i++) {
			JsonObject object =(JsonObject)jsonArray2.get(i);
			System.out.println("NO : "+object.get("NO"));
			System.out.println("NAME : "+object.get("NAME"));
			System.out.println("GENRE : "+object.get("GENRE"));
			System.out.println();
		}
			
		JsonArray jsonArray3=(JsonArray) jsonObj.get("COMPUTER");
		System.out.println("***COMPUTER***");
		for(int i=0;i<jsonArray3.size();i++) {
			JsonObject object =(JsonObject)jsonArray3.get(i);
			System.out.println("NO : "+object.get("NO"));
			System.out.println("NAME : "+object.get("NAME"));
			System.out.println();
		}
		
		
		//CREATE JSON DATA
		JSONObject data=new JSONObject();
		data.put("NO", 1);
		data.put("NAME", "WONJAE");
		
		JSONObject me=new JSONObject();
		me.put("ME", data);
		
		String json=me.toJSONString();
		System.out.println("Created Data : "+json);
		
		//PARSING CREATED JSON DATA
		JSONParser parser=new JSONParser();
		JSONObject object=(JSONObject) parser.parse(json);
		JSONObject parseMe=(JSONObject) object.get("ME");
		int no=((Long)parseMe.get("NO")).intValue();
		String name=(String)parseMe.get("NAME");
		
		System.out.println("parse NO : "+no);
		System.out.println("parse Name : "+name);
		
		
	}

}
