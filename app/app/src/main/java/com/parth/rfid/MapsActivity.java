package com.parth.rfid;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.FragmentActivity;

import android.content.Context;
import android.content.res.Resources;
import android.hardware.usb.UsbDeviceConnection;
import android.hardware.usb.UsbManager;
import android.location.Location;
import android.location.LocationListener;
import android.os.Bundle;
import android.view.View;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.Toast;

import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.api.GoogleApiClient;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MapStyleOptions;
import com.google.android.gms.maps.model.MarkerOptions;
import com.hoho.android.usbserial.driver.UsbSerialDriver;
import com.hoho.android.usbserial.driver.UsbSerialPort;
import com.hoho.android.usbserial.driver.UsbSerialProber;

import java.io.IOException;
import java.util.List;

public class MapsActivity extends FragmentActivity implements OnMapReadyCallback{
    String rfid = "";
    private GoogleMap mMap;
    private Button call_d,call_rfid;
    Location mlocation;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_maps);
        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
        call_d = (Button) findViewById(R.id.request);
        call_rfid = (Button) findViewById(R.id.get_rfid);
        call_d.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (rfid==""){
                    Toast.makeText(MapsActivity.this,"no rfid number",Toast.LENGTH_LONG).show();
                    return;
                }
                String type = "login";
                Toast.makeText(MapsActivity.this,rfid+Integer.toString(rfid.length()),Toast.LENGTH_LONG).show();
                BackgroundWorker backgroundWorker = new BackgroundWorker(MapsActivity.this, mMap,MapsActivity.this,rfid);
                backgroundWorker.execute(type, rfid, rfid);
            }
        });

        call_rfid.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                UsbManager manager = (UsbManager) getSystemService(Context.USB_SERVICE);
                List<UsbSerialDriver> availableDrivers = UsbSerialProber.getDefaultProber().findAllDrivers(manager);
                if (availableDrivers.isEmpty()) {
                    Toast.makeText(MapsActivity.this, "driver not ready",Toast.LENGTH_LONG).show();
                    return;
                }

                UsbSerialDriver driver = availableDrivers.get(0);
                UsbDeviceConnection connection = manager.openDevice(driver.getDevice());
                if (connection == null) {
                    Toast.makeText(MapsActivity.this, "connection not established",Toast.LENGTH_LONG).show();
                    return;
                }

                UsbSerialPort port = driver.getPorts().get(0);
                try {
                    port.open(connection);
                    port.setParameters(9600, 8, UsbSerialPort.STOPBITS_1, UsbSerialPort.PARITY_NONE);
                    byte buffer[] = new byte[16];
                    int numBytesRead = port.read(buffer, 1000);
                    String string = new String(buffer);

                    rfid = string.trim();
                    Toast.makeText(MapsActivity.this, "Read " + numBytesRead + " bytes. "+ string,Toast.LENGTH_LONG).show();
                } catch (IOException e) {
                    // Deal with error.
                } finally {
                    try {
                        port.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }
        });
        mapFragment.getMapAsync(this);
    }


    /**
     * Manipulates the map once available.
     * This callback is triggered when the map is ready to be used.
     * This is where we can add markers or lines, add listeners or move the camera. In this case,
     * we just add a marker near Sydney, Australia.
     * If Google Play services is not installed on the device, the user will be prompted to install
     * it inside the SupportMapFragment. This method will only be triggered once the user has
     * installed Google Play services and returned to the app.
     */
    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;
        try {
            // Customise the styling of the base map using a JSON object defined
            // in a raw resource file.
            boolean success = googleMap.setMapStyle(
                    MapStyleOptions.loadRawResourceStyle(
                            this, R.raw.map_styling));

            if (!success) {
                System.out.println("not success");
            }
        } catch (Resources.NotFoundException e) {
            System.out.println("Can't find style. Error: "+e);
        }
        mMap.animateCamera( CameraUpdateFactory.zoomTo( 7.0f ) );
    }

}
