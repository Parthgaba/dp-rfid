package com.parth.rfid;

import android.Manifest;
import android.app.Activity;
import android.app.AlertDialog;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.AsyncTask;
import android.os.Build;
import android.os.Bundle;
import android.provider.Settings;
import android.view.View;
import android.widget.Toast;

import androidx.core.app.ActivityCompat;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;

import java.io.DataInputStream;
import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

import static android.content.Context.LOCATION_SERVICE;

public class BackgroundWorker extends AsyncTask<String,Void,String> {
    Context context;
    AlertDialog alertDialog;
    GoogleMap nMap;
    Activity act;
    String rfid;

    private LocationManager locationManager;
    private LocationListener listener;
    BackgroundWorker(Context ctx, GoogleMap nMa, Activity activity, String rf) {
        context = ctx;
        nMap = nMa;
        act = activity;
        rfid  = rf;
    }
    @Override
    protected String doInBackground(String... params) {
        String type = params[0];
        if(type.equals("login")) {
            try {
                String ur = "http://dptestparth.000webhostapp.com/query_get.php?query=select * from rfid_data where rfid="+rfid;
                URL url = new URL(ur);
                HttpURLConnection mUrlConnection = (HttpURLConnection) url.openConnection();
                mUrlConnection.setDoInput(true);


                DataInputStream inStream = new DataInputStream(mUrlConnection.getInputStream());
                String inputLine;
                String s="";
                String list[];
                while ((inputLine = inStream.readLine()) != null) {
                    s = s+ inputLine;
                }

                list = s.split(",");
                String ln[] = list[3].split("<br>");
                // Add a marker in Sydney and move the camera
                final LatLng sydney = new LatLng(Double.parseDouble(list[2]),Double.parseDouble(ln[0]));
                final String finalS = s;
                Location locationA = new Location("point A");

                locationA.setLatitude(Double.parseDouble(list[2]));
                locationA.setLongitude(Double.parseDouble(ln[0]));
                Location locationB = new Location("point B");

                locationB.setLatitude(28.721081);
                locationB.setLongitude(77.107047);

                final float distance = locationA.distanceTo(locationB);
                act.runOnUiThread(new Runnable(){
                    public void run(){
                        nMap.addMarker(new MarkerOptions().position(sydney).title(Double.toString(distance)+" m"));
                        nMap.moveCamera(CameraUpdateFactory.newLatLng(sydney));
                        nMap.animateCamera( CameraUpdateFactory.zoomTo( 11.0f ) );
                    }
                });
                return s;
            } catch (MalformedURLException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return null;
    }

    @Override
    protected void onPreExecute() {
        alertDialog = new AlertDialog.Builder(context).create();
        alertDialog.setTitle("Login Status");
    }
    @Override
    protected void onPostExecute(String result) {
        alertDialog.setMessage(result);
        alertDialog.show();
    }

    @Override
    protected void onProgressUpdate(Void... values) {
        super.onProgressUpdate(values);
    }
}