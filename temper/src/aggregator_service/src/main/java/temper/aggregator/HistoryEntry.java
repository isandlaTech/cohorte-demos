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

package temper.aggregator;

/**
 * Definition of an entry in the history of a sensor
 * 
 * @author Thomas Calmant
 */
public class HistoryEntry {

    /** The sensor name */
    private String pName;

    /** The entry time stamp */
    private long pTimestamp;

    /** The unit of the value */
    private String pUnit;

    /** The sensor value */
    private double pValue;

    /**
     * Default constructor (for bean transmission)
     */
    public HistoryEntry() {

        // Do nothing
    }

    /**
     * Retrieves the name of the sensor
     * 
     * @return the sensor name
     */
    public String getName() {

        return pName;
    }

    /**
     * Retrieves the time stamp of the history entry
     * 
     * @return the entry time stamp
     */
    public long getTimestamp() {

        return pTimestamp;
    }

    /**
     * Retrieves the unit of the value
     * 
     * @return the unit
     */
    public String getUnit() {

        return pUnit;
    }

    /**
     * Retrieves the value
     * 
     * @return the value
     */
    public double getValue() {

        return pValue;
    }

    /**
     * Sets the name of the sensor
     * 
     * @param aName
     *            the sensor name
     */
    public void setName(final String aName) {

        pName = aName;
    }

    /**
     * Sets the time stamp of the history entry
     * 
     * @param aTimestamp
     *            the time stamp of the history entry
     */
    public void setTimestamp(final long aTimestamp) {

        pTimestamp = aTimestamp;
    }

    /**
     * Sets the unit of the value
     * 
     * @param aUnit
     *            the unit of the value
     */
    public void setUnit(final String aUnit) {

        pUnit = aUnit;
    }

    /**
     * Sets the value
     * 
     * @param aValue
     *            the value
     */
    public void setValue(final double aValue) {

        pValue = aValue;
    }
}
