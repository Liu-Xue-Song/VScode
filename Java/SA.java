import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
public class SA {
	public static void newp(int a[],int b[],int n)//创造新路径，通过交换某两个点
	{
		if(Math.random()<0.5)
		{
			int p1=(int) (Math.random()*n);
			int p2=(int) (Math.random()*n);
			for(int i=0;i<n;i++)
				b[i]=a[i];
			b[p2]=a[p1];
			b[p1]=a[p2];
		}
		else
		{
			int p1=(int) (Math.random()*n);
			int p2=(int) (Math.random()*n);
			int p3=(int) (Math.random()*n);
			for(int i=0;i<n;i++)
				b[i]=a[i];
			int max=Math.max(p1,p2);
			max=Math.max(max, p3);
			int min=Math.min(p1, p2);
			min=Math.min(min, p3);
			int m=p1+p2+p3-max-min;
			//int x[]=new int[max-m];
			for(int i=0;i<max-m;i++)
				b[i+min]=a[i+m];
			for(int i=0;i<m-min;i++)
				b[i+max-m+min]=a[i+min];
		}
	}
	public static double length(int a[],double d[][],int n)
	{
		double l=0;
		for(int i=0;i<n-1;i++)
			l+=d[a[i]][a[i+1]];
		l+=d[a[n-1]][a[0]];
		return l;
	}
	public static void main(String[] args) throws FileNotFoundException {
		// TODO Auto-generated method stub
		File file=new File("D://Berlin52.txt");
		
		Scanner scan=new Scanner(file);
		String id=file.getName().substring(0, file.getName().lastIndexOf("."));
		String set=file.getParent();
		System.out.println(set);
		System.out.println(id);
		long startTime =  System.currentTimeMillis();
		int n=scan.nextInt();
		int x;
		double a[][]=new double[n][2];
		for(int i=0;i<n;i++)
		{
			//x=scan.nextInt();
			a[i][0]=scan.nextDouble();
			a[i][1]=scan.nextDouble();
			
		}
		scan.close();
		double d[][]=new double[n][n];
		for(int i=0;i<n-1;i++)
			for(int j=i+1;j<n;j++)
			{
				d[i][j]=Math.sqrt((a[i][0]-a[j][0])*(a[i][0]-a[j][0])+(a[i][1]-a[j][1])*(a[i][1]-a[j][1]));
				d[j][i]=d[i][j];
			}
		double t=10000;
		int path[]=new int[n];//最优路径
		double best=1000000;
		for(int i=0;i<n;i++)
			path[i]=i;
		int cur[]=new int[n];
		for(int i=0;i<n;i++)
			cur[i]=i;
		double tf=0;
		while(t>1e-7)//外循环，温度变换
		{
			for(int iter=0;iter<100*n;iter++)//内循环
			{
				int tl=0;
				int np[]=new int[n];
				newp(cur,np,n);
				double nl=length(np,d,n);
				double cl=length(cur,d,n);
				if(nl<cl)//获得更优解则采用
				{
					System.arraycopy(np, 0, cur, 0, n);
					tl=0;
					tf=t;
					if(best>nl)
					{
						best=nl;
						System.arraycopy(cur, 0, path, 0, n);
					}
				}
				else//否则根据概率采用
				{
					if(Math.random()<Math.exp((cl-nl)/t))
						System.arraycopy(np, 0, cur, 0, n);
					tl++;//每次解增大记录加1
				}
				if(tl>500)//连续500次无更优解结束
				{
					//tf++;
					break;
				}
			}
			t*=0.99;
		}
		System.out.println(best);
		int z=0;
		for(int i=0;i<n;i++)
			if(path[i]==0)
			{
				z=i;
				break;
			}
		for(int i=z;i<n;i++)
			System.out.print(path[i]+" ");
		for(int i=0;i<z;i++)
			System.out.print(path[i]+" ");
		System.out.println();
		long endTime =  System.currentTimeMillis();
		long usedTime = (endTime-startTime)/1000;
		System.out.println(usedTime);
	}

}
