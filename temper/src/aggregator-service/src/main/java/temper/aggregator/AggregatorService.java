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

import java.util.List;
import java.util.Map;

public interface AggregatorService {
    /**
     * Retrieves the whole known history
     * 
     * @return the unit of the value
     */
    Map<String, List<HistoryEntry>> getHistory();

    /**
     * Retrieves the history of the given sensor, or null
     * 
     * @param aSensorName
     *            Name of the sensor
     * @return The history of the sensor or null
     */
    List<HistoryEntry> getSensorHistory(String aSensorName);

    /**
     * Retrieves the names of the sensors visible in the history
     * 
     * @return the names of the sensors
     */
    String[] getSensors();
    
    /**
     * Retrieves the names of the active sensors
     * 
     * @return the names of the sensors
     */
    String[] getActiveSensors();
}
