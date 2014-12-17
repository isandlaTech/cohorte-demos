package led.viewers;


import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.lang.reflect.InvocationTargetException;
import java.util.List;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.SwingUtilities;

import org.osgi.service.log.LogService;

import led.services.LedService;

public class Window extends JFrame {

	/**
	 * 
	 */
	private static final long serialVersionUID = 3341532473430415950L;

	private SwingUI sui = null;
	public Window(SwingUI sui) {
		this();
		this.sui = sui;
	}
	
	public Window() {
		super("LED Swing UI");
		try {
			SwingUtilities.invokeAndWait(new Runnable() {
				public void run() {
					initGui();
				}
			});
		} catch (InvocationTargetException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	
	/**
	 * Updates the list of LEDs on the window.
	 */
    public void updateLEDs(List<LedService> aLeds) {
    	int index = 1;
    	Window.this.getContentPane().removeAll();
    	for (LedService led : aLeds) {	    	
	    	newLED(led, index);   
	    	index++;
    	}
    	Window.this.pack();	
    }
    
    /**
     * Adds a new LED to the window.
     * @param name
     * @param state
     * @param num incremental number to place the LEDs on the window's grid.
     */
    private void newLED(LedService led, int num) {
    	this.sui.getLogger().log(LogService.LOG_ERROR, "Adding LED " + led.toString());
    	JLabel ledName = new JLabel("LED"/*led.getName()*/);
		GridBagConstraints gbc_lbl = new GridBagConstraints();
		gbc_lbl.anchor = GridBagConstraints.WEST;
		gbc_lbl.insets = new Insets(5, 5, 5, 5);
		gbc_lbl.gridx = 0;
		gbc_lbl.gridy = num;
		Window.this.getContentPane().add(ledName, gbc_lbl);
		
		JButton btnOn_1 = new JButton("ON");
		GridBagConstraints gbc_btnOn_1 = new GridBagConstraints();
		gbc_btnOn_1.insets = new Insets(0, 0, 5, 5);
		gbc_btnOn_1.gridx = 1;
		gbc_btnOn_1.gridy = num;
		
		final LedService myled = led;
		
		btnOn_1.addActionListener(new ActionListener() {			
			public void actionPerformed(ActionEvent e) {
				Window.this.sui.getLogger().log(LogService.LOG_ERROR, "ON button clicked!");
				if (myled != null) {					
					Window.this.sui.getLogger().log(LogService.LOG_ERROR, "Trying to turn LED ON");
					try {
						myled.on();
					} catch (Throwable ex) {
						Window.this.sui.getLogger().log(LogService.LOG_ERROR, "Error calling ON" + ex, ex);
					}
					Window.this.sui.getLogger().log(LogService.LOG_ERROR, "LED turned ON");
				} else {
					Window.this.sui.getLogger().log(LogService.LOG_ERROR, "LED service not available.");
				}
			}
		});
		Window.this.getContentPane().add(btnOn_1, gbc_btnOn_1);
		
		JButton btnOff_1 = new JButton("OFF");
		GridBagConstraints gbc_btnOff_1 = new GridBagConstraints();
		gbc_btnOff_1.insets = new Insets(0, 0, 5, 0);
		gbc_btnOff_1.gridx = 2;
		gbc_btnOff_1.gridy = num;
		btnOff_1.addActionListener(new ActionListener() {			
			public void actionPerformed(ActionEvent e) {
				Window.this.sui.getLogger().log(LogService.LOG_ERROR, "OFF button clicked!");
				if (myled != null) {					
					Window.this.sui.getLogger().log(LogService.LOG_ERROR, "Trying to turn LED OFF");
					try {
						myled.off();
					} catch (Throwable ex) {
						Window.this.sui.getLogger().log(LogService.LOG_ERROR, "Error calling ON" + ex, ex);
					}
					Window.this.sui.getLogger().log(LogService.LOG_ERROR, "LED turned OFF");
				} else {
					Window.this.sui.getLogger().log(LogService.LOG_ERROR, "LED service not available.");
				}
			}
		});
		Window.this.getContentPane().add(btnOff_1, gbc_btnOff_1);
    }
    
    /**
     * Initialize the Graphical User Interface
     */
    private void initGui() {
		GridBagLayout gridBagLayout = new GridBagLayout();
		gridBagLayout.columnWidths = new int[] {125, 0, 75};
		gridBagLayout.rowHeights = new int[]{29, 0, 0, 0};
		gridBagLayout.columnWeights = new double[]{0.0, 0.0, 0.0};
		gridBagLayout.rowWeights = new double[]{0.0, 0.0, 0.0, Double.MIN_VALUE};
		Window.this.getContentPane().setLayout(gridBagLayout);		
		Window.this.getContentPane().addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {			
				super.mouseClicked(e);
				Window.this.updateLEDs(Window.this.sui.getLeds());
			}
		});
		Window.this.getContentPane().addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				updateLEDs(Window.this.sui.getLeds());
			}
		});
		Window.this.pack();		
	}
}
