package guiEvent;

import java.awt.FileDialog;
import java.awt.Frame;
import java.awt.Menu;
import java.awt.MenuBar;
import java.awt.MenuItem;
import java.awt.TextArea;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
 
public class TextEditor {
 
	private Frame f;
	private TextArea ted;
	public TextEditor(){
		f = new Frame("简单文本编辑器");
		f.setBounds(100, 100, 200, 200);
		//Menu无法直接添加到容器中，只能直接添加到菜单容器中
		MenuBar mb = new MenuBar(); //创建菜单容器
		f.setMenuBar(mb);
		//添加菜单
		Menu m1 = new Menu("File");
		Menu m2 = new Menu("Edit");
		Menu m3 = new Menu("Help");
		mb.add(m1);
		mb.add(m2);
		mb.add(m3);
		
		//添加菜单项
		MenuItem mi1 = new MenuItem("Save");
		MenuItem mi2 = new MenuItem("Load");
		MenuItem mi3 = new MenuItem("Quit");
		m1.add(mi1);
		m1.add(mi2);
		m1.addSeparator(); //添加分隔线
		m1.add(mi3);
		
		ted = new TextArea("",10,10);
		f.add("Center",ted);
		
		f.setVisible(true);
		
		//窗口事件监听-关闭
		f.addWindowListener(new WindowAdapter() {
			public void windowClosing(WindowEvent e){
				System.exit(1);
			}
		});
		//事件监听:如果直接在当前类上继承或实现监听，则此处使用this
		mi1.addActionListener(new MenuListener());
		mi2.addActionListener(new MenuListener());
		mi3.addActionListener(new MenuListener());
	}
	
	//菜单选项监听器
	class MenuListener implements ActionListener{
 
		@Override
		public void actionPerformed(ActionEvent e) {
			// 操作的组件是谁，就返回谁
			MenuItem i = (MenuItem) e.getSource();
			if("Quit".equals(i.getLabel())){
				System.exit(1);
			}else if("Save".equals(i.getLabel())){
				SaveFile();
			}else if("Load".equals(i.getLabel())){
				loadFile();
			}
		}
		
	}
	
	/**
	 * 保存文件方法
	 */
	void SaveFile(){
		FileDialog fd = new FileDialog(f,"请输入要保存的文件名",FileDialog.SAVE);
		fd.setVisible(true);
		if(fd==null || fd.getFile()==null || "".equals(fd.getFile())){
			return;
		}
		String fileName = fd.getFile();
		String filePath = fd.getDirectory()+fileName;
		try {
			FileOutputStream fos = new FileOutputStream(filePath);
			OutputStreamWriter ows = new OutputStreamWriter(fos);
			ows.write(ted.getText());
			ows.flush();
			ows.close();
			fos.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	/**
	 * 文件读取方法
	 */
	void loadFile(){
		FileDialog fd = new FileDialog(f,"请选择要读取的文件",FileDialog.LOAD);
		fd.setVisible(true);
		if(fd==null || fd.getFile()==null || "".equals(fd.getFile())){
			return;
		}
		ted.setText("");
		String fileName = fd.getFile();
		String filePath = fd.getDirectory()+fileName;
		try {
			BufferedReader in = new BufferedReader(new FileReader(filePath));
			String line = null;
            while ((line = in.readLine()) != null)
            {
               ted.setText(ted.getText() + line+ System.getProperty("line.separator"));
            }
            in.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
		new TextEditor();
	}
 
}