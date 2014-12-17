/**
 * Copyright 2014 isandlaTech
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package led.viewers;

import java.lang.reflect.InvocationTargetException;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JOptionPane;
import javax.swing.SwingUtilities;

import led.services.LedService;

import org.apache.felix.ipojo.annotations.Bind;
import org.apache.felix.ipojo.annotations.Component;
import org.apache.felix.ipojo.annotations.Invalidate;
import org.apache.felix.ipojo.annotations.Requires;
import org.apache.felix.ipojo.annotations.Unbind;
import org.apache.felix.ipojo.annotations.Validate;
import org.osgi.service.log.LogService;

/**
 * Swing UI for viewing and controlling LEDs
 * 
 * @author Bassem Debbabi
 */
@Component(name="java_swing_ui_factory")
public class SwingUI {

	private Window pWindow;
	private Boolean isValid = false;
	@Requires
	private LogService logger;
	
	private List<LedService> pLeds = new ArrayList<LedService>();
	
	public SwingUI() {
		pWindow = new Window(this);
	}

	public List<LedService> getLeds() {
		return this.pLeds;
	}
	
	public LogService getLogger() {
		return this.logger;
	}
	
    @Bind(optional=true)
    public synchronized void bindLed(final LedService led) {
    	
    	if (led != null)
    		logger.log(LogService.LOG_ERROR, "new led service detected! ");    	
        this.pLeds.add(led);
        if (isValid == true)
        	this.pWindow.updateLEDs(this.pLeds);
    }

    @Unbind
    public synchronized void unbindLed(LedService led) {
        this.pLeds.remove(led);
        if (isValid == true)
        	this.pWindow.updateLEDs(this.pLeds);
    }
	
	/**
     * Component validation
     */
    @Validate
    public void validate() {    	
    	Thread t = new Thread(new Runnable() {			
			public void run() {				
				try {
					Thread.sleep(2000);
				} catch (InterruptedException e) {					
					e.printStackTrace();
				}
				isValid = true;
		    	if (pWindow != null) {
		    		pWindow.setVisible(true);
		    	}	
		    	pWindow.updateLEDs(pLeds);
			}
		});
    	t.start();
    }
    
    /**
     * Component invalidation
     */
    @Invalidate
    public void invalidate() {
    	if (this.pWindow != null) {
    		this.pWindow.setVisible(false);
    	}
    }



}
