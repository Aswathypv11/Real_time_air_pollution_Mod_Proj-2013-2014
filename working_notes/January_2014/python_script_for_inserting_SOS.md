**python_script_for_inserting_SOS**

A python script to insert data into 52 NORTH SOS through HTTP POST. Save this script as python file and run the script in terminal as python “scriptname”.py. It will insert the data and report the status as given by test client “send” button. 52 north SOS has to be run in localhost.

based on
https://github.com/mpfeil/qualitySCHU/blob/master/Parser/LANUV/main.py 
http://stackoverflow.com/questions/16055334/post-xml-request-using-python

```
import urllib 
import httplib from xml.dom.minidom 
import parse, parseString
target_url = “http://localhost:8080/52n-sos-webapp-4.0.0-Beta1/sos/soap” #the insert observation requests from test client 52 north SOS xml_request = “”"

        <sos:offering>test_offering_1</sos:offering>
        <sos:observation>
            <om:OM_Observation gml:id="o1">
                <om:type xlink:href="http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement"/>
                <om:phenomenonTime>
                    <gml:TimeInstant gml:id="phenomenonTime">
                        <gml:timePosition>2013-12-14T17:45:15.000+00:00</gml:timePosition>
                    </gml:TimeInstant>
                </om:phenomenonTime>
                <om:resultTime xlink:href="#phenomenonTime"/>
                <om:procedure xlink:href="http://www.example.org/sensors/101"/>
                <om:observedProperty xlink:href="test_observable_property_1"/>
                <om:featureOfInterest>
                    <sams:SF_SpatialSamplingFeature gml:id="ssf_test_feature_1">
                        <gml:identifier codeSpace="">test_feature_1</gml:identifier>
                        <sf:type xlink:href="http://www.opengis.net/def/samplingFeatureType/OGC-OM/2.0/SF_SamplingPoint"/>
                        <sf:sampledFeature xlink:href="test_feature_1"/>
                        <sams:shape>
                            <gml:Point gml:id="test_feature_1">
                                <gml:pos srsName="http://www.opengis.net/def/crs/EPSG/0/4326">49.594538 20.401108</gml:pos>
                            </gml:Point>
                        </sams:shape>
                    </sams:SF_SpatialSamplingFeature>
                </om:featureOfInterest>
                <om:result xsi:type="gml:MeasureType" uom="urn:ogc:def:uom:OGC:m">4444</om:result>
            </om:OM_Observation>
        </sos:observation>
    </sos:InsertObservation>
</env:Body>

“”" def send_xml(): result = urllib.urlopen( target_url, urllib.urlencode( {‘request’:xml_request} ) ) #parse results and print the xml # or do whatever with it dom = parse( result ) print dom.toprettyxml() result.close()
def main(): send_xml()
if name == “main”: main()
```