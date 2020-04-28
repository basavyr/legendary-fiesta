#include <iostream>
#include <fstream>
#include <vector>
#include <ctime>
#include <string>
#include <cmath>

inline void newline()
{
    std::cout << "\n";
}

const double pi = 3.141592654;

double j_Component(int k, double theta)
{
    const double j = 5.5;
    if (k == 1)
        return static_cast<double>(j * cos(theta * pi / 180.0));
    return static_cast<double>(j * (sin(theta * pi / 180.0)));
}

double A_fct(double spin, double a1, double a2, double theta)
{
    auto j2 = j_Component(2, theta);
    auto result = a2 * (1 - j2 / spin) - a1;
    return static_cast<double>(result);
}

double v0_Fct(double spin, double a1, double a2, double theta)
{
    auto j1 = j_Component(1, theta);
    auto result = (-a1 * j1) / A_fct(spin, a1, a2, theta);
    return static_cast<double>(result);
}

double u_Fct(double spin, double a1, double a2, double a3, double theta)
{
    auto result = (a3 - a1) / A_fct(spin, a1, a2, theta);
    return static_cast<double>(result);
}

struct sphericalCoordinates
{
    double x1;
    double x2;
    double x3;
    sphericalCoordinates()
    {
        x1 = 0.0;
        x2 = 0.0;
        x3 = 0.0;
    }
};

double H_Classic(double spin, sphericalCoordinates I, double u, double v0)
{
    auto result = pow(I.x2, 2) + u * pow(I.x3, 2) + 2.0 * v0 * I.x1;
    return static_cast<double>(result);
}

double H_Prime1(double spin, sphericalCoordinates I, double u, double v0, double fi)
{
    fi = fi * pi / 180.0;
    auto energy = (pow(cos(fi), 2) + u * pow(sin(fi), 2)) * (pow(spin, 2) - pow(I.x1, 2)) + 2.0 * v0 * I.x1;
    return static_cast<double>(energy);
}

double H_Prime2(double spin, sphericalCoordinates I, double u, double v0, double fi)
{
    fi = fi * pi / 180.0;
    auto energy = pow(I.x2, 2) * (1.0 - u * pow(cos(fi), 2) - v0 / spin * sin(fi)) + u * pow(spin, 2) * pow(cos(fi), 2) + 2.0 * v0 * spin * sin(fi);
    return static_cast<double>(energy);
}

double H_Prime3(double spin, sphericalCoordinates I, double u, double v0, double fi)
{
    fi = fi * pi / 180.0;
    auto energy = pow(I.x3, 2) * (u - pow(sin(fi), 2) - v0 / spin * cos(fi)) + pow(spin, 2) * pow(sin(fi), 2) + 2.0 * v0 * spin * cos(fi);
    return static_cast<double>(energy);
}

sphericalCoordinates quantization(int k, double r, double theta, double fi)
{
    theta = theta * pi / 180.0;
    fi = fi * pi / 180.0;
    auto am = new sphericalCoordinates();
    if (k == 1)
    {
        am->x1 = r * cos(theta);
        am->x2 = r * sin(theta) * cos(fi);
        am->x3 = r * sin(theta) * sin(fi);
    }
    else if (k == 2)
    {
        am->x2 = r * cos(theta);
        am->x1 = r * sin(theta) * sin(fi);
        am->x3 = r * sin(theta) * cos(fi);
    }
    else if (k == 3)
    {
        am->x3 = r * cos(theta);
        am->x1 = r * sin(theta) * cos(fi);
        am->x2 = r * sin(theta) * sin(fi);
    }
    return *am;
}

void CalculateEnergies(const int axis)
{
    //constants
    const double spin = 9.5;
    const double theta = 45.0;
    double A1, A2, A3;

    auto u = [&](auto x) {
        return u_Fct(x, A1, A2, A3, theta);
    };
    auto v0 = [&](auto x) {
        return v0_Fct(x, A1, A2, theta);
    };

    const double thetaSph = 30.0;
    const double fiSph = 20.0;
    auto I = sphericalCoordinates();

    double energyClassical;
    double energySpherical;
    double energyAnalytic;
    std::cout << "Quantization on " << axis << "-axis";
    newline();
    switch (axis)
    {
    case 1:
        A1 = 1.0;
        A2 = 6.0;
        A3 = 3.0;
        I = quantization(axis, spin, thetaSph, fiSph);
        std::cout << u(spin) << " " << v0(spin);
        newline();
        std::cout << I.x1 << " " << I.x2 << " " << I.x3;
        newline();
        energyClassical = H_Classic(spin, I, u(spin), v0(spin));
        energySpherical = H_Prime1(spin, I, u(spin), v0(spin), fiSph);
        std::cout << energyClassical << " " << energySpherical;
        newline();
        break;
    case 2:
        A2 = 1.0;
        A1 = 3.0;
        A3 = 6.0;
        I = quantization(axis, spin, thetaSph, fiSph);
        std::cout << u(spin) << " " << v0(spin);
        newline();
        std::cout << I.x1 << " " << I.x2 << " " << I.x3;
        newline();
        energyClassical = H_Classic(spin, I, u(spin), v0(spin));
        energySpherical = H_Prime2(spin, I, u(spin), v0(spin), fiSph);
        std::cout << energyClassical << " " << energySpherical;;
        newline();
        break;
    case 3:
        A1 = 6.0;
        A2 = 3.0;
        A3 = 1.0;
        I = quantization(axis, spin, thetaSph, fiSph);
        std::cout << u(spin) << " " << v0(spin);
        newline();
        std::cout << I.x1 << " " << I.x2 << " " << I.x3;
        newline();
        energyClassical = H_Classic(spin, I, u(spin), v0(spin));
        energySpherical = H_Prime3(spin, I, u(spin), v0(spin), fiSph);
        std::cout << energyClassical << " " << energySpherical;
        newline();
        break;
    default:
        break;
    }
}

int main()
{
    CalculateEnergies(1);
    CalculateEnergies(2);
    CalculateEnergies(3);
}