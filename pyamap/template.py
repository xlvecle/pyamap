#coding: utf-8
html = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Show Pos</title>   
    <script id="jquery_172" type="text/javascript" class="library" src="js/jquery-1.8.0.min.js"></script>
    <style type="text/css">
      body{
        margin:0;
        height:100%;
        width:100%;
        position:absolute;
      }
      #mapContainer{
        width: 100%;
        height: 100%;
      }
    </style>
  </head>
  <body>
    <div id="mapContainer"></div>
    <script type="text/javascript" src="http://webapi.amap.com/maps?v=1.3&key=820afe3932ebea15d73cd05b2a28e606";></script>
    <script type="text/javascript" src="js/pos.js"></script>
    <script type="text/javascript">
        var zoomLevel = //ZOOM_LEVEL//;

        var map, marker;
        //初始化地图对象，加载地图
        map = new AMap.Map("mapContainer",{
          resizeEnable: true,
          //二维地图显示视口
          view: new AMap.View2D({
            center:new AMap.LngLat(116.397428,39.90923),//地图中心点
            zoom: zoomLevel //地图显示的缩放级别
          })
        }); 
        
        //实例化点标记
        function addMarker(x, y){
          var marker = new AMap.Marker({          
            icon:"http://webapi.amap.com/images/marker_sprite.png",
            position:new AMap.LngLat(x, y)
          });
          marker.setMap(map);  //在地图上添加点
        }
        // 添加多边形
        function addPolygon(polygonArr) {
          polygon = new AMap.Polygon({
              path: polygonArr,//设置多边形边界路径
              strokeColor: "#FF33FF", //线颜色
              strokeOpacity: 0.2, //线透明度
              strokeWeight: 3,    //线宽
              fillColor: "#1791fc", //填充色
              fillOpacity: 0.35//填充透明度
          });
          polygon.setMap(map);
          map.setZoomAndCenter(zoomLevel, polygonArr[0])     
        }
        //添加圆点  
        function addCircle(x, y) {  
           circle = new AMap.Circle({   
           center:new AMap.LngLat(x, y),// 圆心位置  
           radius:100, //半径  
           strokeColor: "blue", //线颜色  
           strokeOpacity: 1, //线透明度  
           strokeWeight: 3, //线粗细度  
           fillColor: "#F33", //填充颜色  
           fillOpacity: 3//填充透明度  
           });   
           circle.setMap(map);
           map.setZoomAndCenter(zoomLevel, [x,y])     
        }
    </script>
    <script type="text/javascript">
      //for PyAmap//
    </script>
  </body>
</html>

"""