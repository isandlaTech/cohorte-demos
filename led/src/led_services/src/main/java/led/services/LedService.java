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

package led.services;

public interface LedService {

    /**
     * Gets the symbolic name of the LED
     * 
     * @return symbolic name
     */
    String getName();
    
	/**
     * Gets the actual state of the LED
     * 
     * @return the state of the LED as a string ("on" or "off")
     */
    String getState();

    /**
     * Sets the LED state to ON (switch on the LED)
     * 
     */
    void on();

    /**
     * Sets the LED state to OFF (switch off the LED)
     * 
     */
    void off();
}
